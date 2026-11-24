#!/usr/bin/env bash
# Puts CaptCan TV on the shop Fire TV Stick from the Mac mini, and lets it start by itself at power-on.
# Use:  bash install.sh 192.168.x.x      (the stick's IP: Settings > My Fire TV > About > Network)
# Needs: adb (brew install android-platform-tools) and "ADB debugging" turned ON on the stick.
set -euo pipefail
IP="${1:?Give the Fire TV Stick IP address, e.g. bash install.sh 192.168.1.50}"
PKG=ca.captcancomics.tv
APK="$(mktemp -t captcan-tv).apk"
curl -fsSL -o "$APK" "https://rdjmitch.github.io/captcan-tv/app/captcan-tv.apk?t=$(date +%s)"
adb connect "$IP:5555"            # first time: the TV shows "Allow USB debugging?"  tick Always allow, press OK
sleep 2
adb -s "$IP:5555" uninstall "$PKG" >/dev/null 2>&1 || true      # builds are signed with a fresh key each time
adb -s "$IP:5555" install "$APK"
adb -s "$IP:5555" shell cmd appops set "$PKG" SYSTEM_ALERT_WINDOW allow   # lets it start at power-on (Fire OS 8)
adb -s "$IP:5555" shell am start -n "$PKG/.MainActivity"
echo "CaptCan TV is installed and running. It will start by itself when the stick powers on."
