package ca.captcancomics.tv;

import android.app.AlarmManager;
import android.app.PendingIntent;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.SystemClock;

/* Starts CaptCan TV when the stick powers on. Fire OS 8 only allows this after the one-time
   "appops set ca.captcancomics.tv SYSTEM_ALERT_WINDOW allow" command (see README).
   The Fire TV home screen comes up after boot and covers anything started too early,
   so the start is repeated at 12, 35 and 80 seconds. */
public class BootReceiver extends BroadcastReceiver {
  @Override public void onReceive(Context c, Intent i) {
    try {
      Intent s = new Intent(c, MainActivity.class);
      s.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TOP);
      s.putExtra("boot", true);
      c.startActivity(s);
    } catch (Throwable t) { /* not allowed yet: the app still opens from the home row */ }
    try {
      AlarmManager am = (AlarmManager) c.getSystemService(Context.ALARM_SERVICE);
      int[] secs = {12, 35, 80};
      for (int n = 0; n < secs.length; n++) {
        Intent s = new Intent(c, MainActivity.class);
        s.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_SINGLE_TOP);
        PendingIntent pi = PendingIntent.getActivity(c, 20 + n, s, PendingIntent.FLAG_UPDATE_CURRENT | PendingIntent.FLAG_IMMUTABLE);
        am.setExact(AlarmManager.ELAPSED_REALTIME_WAKEUP, SystemClock.elapsedRealtime() + secs[n] * 1000L, pi);
      }
    } catch (Throwable t) {}
  }
}
