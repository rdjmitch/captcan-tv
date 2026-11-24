package ca.captcancomics.tv;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;

/* Starts CaptCan TV when the stick powers on. Fire OS 8 only allows this after the one-time
   "appops set ca.captcancomics.tv SYSTEM_ALERT_WINDOW allow" command (see README). */
public class BootReceiver extends BroadcastReceiver {
  @Override public void onReceive(Context c, Intent i) {
    try {
      Intent s = new Intent(c, MainActivity.class);
      s.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TOP);
      s.putExtra("boot", true);
      c.startActivity(s);
    } catch (Throwable t) { /* not allowed yet: the app still opens from the home row */ }
  }
}
