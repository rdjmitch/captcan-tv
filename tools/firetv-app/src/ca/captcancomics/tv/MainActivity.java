package ca.captcancomics.tv;

import android.app.Activity;
import android.graphics.Color;
import android.net.http.SslError;
import android.os.Build;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.os.SystemClock;
import android.view.Gravity;
import android.view.KeyEvent;
import android.view.View;
import android.view.ViewGroup;
import android.view.WindowManager;
import android.webkit.JavascriptInterface;
import android.webkit.PermissionRequest;
import android.webkit.RenderProcessGoneDetail;
import android.webkit.SslErrorHandler;
import android.webkit.WebChromeClient;
import android.webkit.WebResourceError;
import android.webkit.WebResourceRequest;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.FrameLayout;
import android.widget.TextView;

/* CaptCan TV for Fire TV: one full-screen page, sound allowed without a button press,
   screen kept awake, reloads itself if the page stops or the network drops. */
public class MainActivity extends Activity {
  /* First choice: the copy served by the Mac mini on the shop network (clips play from files there).
     If the Mac mini cannot be reached, the internet copy runs instead and the Mac mini is tried again every 10 minutes. */
  static final String HOME = "http://192.168.50.253:8788/?tv&app=" + BuildInfo.VERSION;
  static final String NET = "https://rdjmitch.github.io/captcan-tv/?tv&nohome&app=" + BuildInfo.VERSION;
  boolean onNet = false; long netSince = 0, homeFails = 0;
  static final long STALL_MS = 4 * 60 * 1000;      // no heartbeat from the page for this long = reload
  static final long AWAY_RELOAD_MS = 10 * 60 * 1000; // back from sleep after this long = fresh load

  final Handler h = new Handler(Looper.getMainLooper());
  FrameLayout root; WebView web; TextView note;
  long lastBeat = 0, pausedAt = 0, lastBack = 0; boolean pageOk = false, errored = false, leaving = false; int retry = 0;

  @Override protected void onCreate(Bundle b) {
    super.onCreate(b);
    getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON | WindowManager.LayoutParams.FLAG_FULLSCREEN);
    root = new FrameLayout(this); root.setBackgroundColor(Color.BLACK);
    note = new TextView(this); note.setTextColor(0xFF8A8A92); note.setTextSize(22); note.setGravity(Gravity.CENTER);
    note.setText("CaptCan TV is starting");
    setContentView(root);
    build();
    h.postDelayed(watch, 30000);
  }

  void build() {
    root.removeAllViews();
    if (web != null) { try { web.destroy(); } catch (Throwable t) {} }
    web = new WebView(this);
    web.setBackgroundColor(Color.BLACK);
    WebSettings s = web.getSettings();
    s.setJavaScriptEnabled(true);
    s.setDomStorageEnabled(true);
    s.setDatabaseEnabled(true);
    s.setMediaPlaybackRequiresUserGesture(false);
    s.setLoadWithOverviewMode(false);
    s.setUseWideViewPort(true);
    s.setSupportZoom(false);
    s.setCacheMode(WebSettings.LOAD_DEFAULT);
    s.setMixedContentMode(WebSettings.MIXED_CONTENT_COMPATIBILITY_MODE);
    s.setUserAgentString(s.getUserAgentString() + " CaptCanTVApp/" + BuildInfo.VERSION);
    web.setOverScrollMode(View.OVER_SCROLL_NEVER);
    web.setVerticalScrollBarEnabled(false); web.setHorizontalScrollBarEnabled(false);
    web.setFocusable(true); web.setFocusableInTouchMode(true);
    web.addJavascriptInterface(new Bridge(), "CaptCanTVApp");
    web.setWebChromeClient(new WebChromeClient() {
      @Override public void onPermissionRequest(PermissionRequest r) { try { r.deny(); } catch (Throwable t) {} }
    });
    web.setWebViewClient(new WebViewClient() {
      @Override public boolean shouldOverrideUrlLoading(WebView v, WebResourceRequest r) {
        String host = r.getUrl().getHost(); if (host == null) return true;
        // the channel only ever lives on these two hosts; anything else is ignored
        return !(host.equals("rdjmitch.github.io") || host.endsWith("captcancomics.ca") || host.startsWith("192.168.") || host.startsWith("10."));
      }
      @Override public void onPageFinished(WebView v, String url) {
        if (!errored && url != null && url.startsWith("https")) { pageOk = true; retry = 0; lastBeat = SystemClock.elapsedRealtime(); note.setVisibility(View.GONE); v.requestFocus(); }
      }
      @Override public void onReceivedError(WebView v, WebResourceRequest r, WebResourceError e) {
        if (r.isForMainFrame()) failed();
      }
      @Override public void onReceivedSslError(WebView v, SslErrorHandler hd, SslError e) { hd.cancel(); }
      @Override public boolean onRenderProcessGone(WebView v, RenderProcessGoneDetail d) {
        h.post(new Runnable() { public void run() { build(); } });
        return true;
      }
    });
    root.addView(web, new FrameLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT));
    root.addView(note, new FrameLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT));
    note.setVisibility(View.VISIBLE);
    load();
  }

  void load() { pageOk = false; errored = false; h.removeCallbacks(again); lastBeat = SystemClock.elapsedRealtime();
    if (onNet && SystemClock.elapsedRealtime() - netSince > 10 * 60 * 1000) onNet = false;   // time to try the Mac mini again
    web.loadUrl((onNet ? NET : HOME) + "&t=" + System.currentTimeMillis()); }

  /* no network yet (common right after power-on): keep the screen black and try again, quickly at first */
  void failed() {
    pageOk = false; errored = true; retry++;
    if (!onNet) { homeFails++; if (homeFails >= 2) { onNet = true; netSince = SystemClock.elapsedRealtime(); homeFails = 0; h.removeCallbacks(again); h.postDelayed(again, 1500); return; } }
    note.setVisibility(View.VISIBLE); note.setText("CaptCan TV is waiting for the internet");
    try { web.loadUrl("about:blank"); } catch (Throwable t) {}
    h.removeCallbacks(again);
    h.postDelayed(again, retry < 12 ? 5000 : 30000);
  }
  final Runnable again = new Runnable() { public void run() { load(); } };

  final Runnable watch = new Runnable() { public void run() {
    try {
      if (pausedAt == 0 && pageOk && SystemClock.elapsedRealtime() - lastBeat > STALL_MS) load();
      else if (pausedAt == 0 && pageOk && onNet && SystemClock.elapsedRealtime() - netSince > 10 * 60 * 1000) load();
    } catch (Throwable t) {}
    h.postDelayed(this, 30000);
  } };

  class Bridge {
    @JavascriptInterface public void beat() { lastBeat = SystemClock.elapsedRealtime(); }
    @JavascriptInterface public String info() { return "app " + BuildInfo.VERSION + " " + Build.MODEL + " os" + Build.VERSION.SDK_INT; }
    @JavascriptInterface public void reload() { h.post(new Runnable() { public void run() { load(); } }); }
  }

  void immersive() {
    getWindow().getDecorView().setSystemUiVisibility(View.SYSTEM_UI_FLAG_LAYOUT_STABLE | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
      | View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN | View.SYSTEM_UI_FLAG_HIDE_NAVIGATION | View.SYSTEM_UI_FLAG_FULLSCREEN
      | View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY);
  }

  @Override public void onWindowFocusChanged(boolean f) { super.onWindowFocusChanged(f); if (f) { immersive(); if (web != null) web.requestFocus(); } }

  @Override protected void onResume() {
    super.onResume(); immersive();
    if (web != null) { web.onResume(); web.resumeTimers(); }
    if (pausedAt > 0 && SystemClock.elapsedRealtime() - pausedAt > AWAY_RELOAD_MS) load();
    pausedAt = 0; lastBeat = SystemClock.elapsedRealtime();
  }

  @Override protected void onPause() { super.onPause(); pausedAt = SystemClock.elapsedRealtime(); if (web != null) web.onPause(); }

  /* If someone presses Home by accident, the channel comes back by itself after 3 minutes.
     Pressing Back twice is the deliberate way out and does not come back. */
  android.app.PendingIntent returnIntent() {
    android.content.Intent i = new android.content.Intent(this, MainActivity.class);
    i.addFlags(android.content.Intent.FLAG_ACTIVITY_NEW_TASK | android.content.Intent.FLAG_ACTIVITY_SINGLE_TOP);
    return android.app.PendingIntent.getActivity(this, 7, i, android.app.PendingIntent.FLAG_UPDATE_CURRENT | android.app.PendingIntent.FLAG_IMMUTABLE);
  }
  void cancelReturn() { try { ((android.app.AlarmManager) getSystemService(ALARM_SERVICE)).cancel(returnIntent()); } catch (Throwable t) {} }
  @Override protected void onStop() { super.onStop();
    if (!leaving) { try { ((android.app.AlarmManager) getSystemService(ALARM_SERVICE)).set(android.app.AlarmManager.ELAPSED_REALTIME_WAKEUP, SystemClock.elapsedRealtime() + 3 * 60 * 1000, returnIntent()); } catch (Throwable t) {} } }
  @Override protected void onStart() { super.onStart(); leaving = false; cancelReturn(); }

  @Override protected void onDestroy() { h.removeCallbacksAndMessages(null); if (web != null) { try { web.destroy(); } catch (Throwable t) {} } super.onDestroy(); }

  /* Back never closes the channel by accident: press Back twice within 2 seconds to leave. Menu (three lines) reloads. */
  @Override public boolean dispatchKeyEvent(KeyEvent e) {
    if (e.getAction() == KeyEvent.ACTION_DOWN) {
      int k = e.getKeyCode();
      if (k == KeyEvent.KEYCODE_BACK) {
        long n = SystemClock.elapsedRealtime();
        if (n - lastBack < 2000) { leaving = true; cancelReturn(); finish(); } else { lastBack = n; }
        return true;
      }
      if (k == KeyEvent.KEYCODE_MENU) { load(); return true; }
    }
    return super.dispatchKeyEvent(e);
  }
}
