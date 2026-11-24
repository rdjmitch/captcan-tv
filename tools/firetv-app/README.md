# CaptCan TV app for the Fire TV Stick

A tiny app that only opens the CaptCan TV page. Compared with the Silk browser it gives:

- full screen straight away, no browser bar
- sound without anyone pressing OK
- the screen never sleeps while the channel is up
- it starts by itself when the stick powers on (after the one-time step below)
- it reloads by itself if the page stops, the internet drops, or the stick wakes from a long sleep
- Back does nothing unless pressed twice (so the channel is not closed by accident); the Menu button reloads

The app shows whatever is live at https://rdjmitch.github.io/captcan-tv/ so changing the channel never needs a new app.

## Build
GitHub builds it on every change in this folder (`.github/workflows/firetv-app.yml` runs `build.sh`) and saves
`app/captcan-tv.apk` in the repo. No signing key is stored: each build makes a one-off key, so a newer build is
installed by removing the old app first (`install.sh` does this).

## Install (one time, from the Mac mini)
On the stick (needs the parental PIN; reset it at amazon.com/pin if it is unknown):
1. Settings > My Fire TV > About: click "Fire TV Stick 4K Max" seven times until it says "you are now a developer".
2. Settings > My Fire TV > Developer options: turn ON "ADB debugging".
3. Settings > My Fire TV > About > Network: note the IP address.

On the Mac mini: `bash install.sh <that IP>`. The TV asks "Allow USB debugging?" once: tick "Always allow", press OK.
The script installs the app, allows it to start at power-on (Fire OS 8 needs
`appops set ca.captcancomics.tv SYSTEM_ALERT_WINDOW allow`, which only works over ADB) and opens it.

## Not yet proven on the real stick
Built and compiled, never run on the device as of Nov 24 2026. Check on first install: YouTube clips play inside the
app, sound starts with no press, and the app comes up by itself after unplugging and replugging the stick.
