#!/bin/bash
# CaptCan TV: turns this Mac mini into the TV's source. Run once; it restarts by itself after a reboot.
cd "$(dirname "$0")" || exit 1
DIR="$(pwd)"; LABEL="ca.captcancomics.tv"; PLIST="$HOME/Library/LaunchAgents/$LABEL.plist"
PY=""
for c in "$HOME/.homebrew/bin/python3" /opt/homebrew/bin/python3 /usr/local/bin/python3 /usr/bin/python3; do
  if [ -x "$c" ] && "$c" -c "import http.server" >/dev/null 2>&1; then PY="$c"; break; fi
done
if [ -z "$PY" ]; then echo "No Python found on this Mac. Tell Claude: 'no python'."; echo "no python" > "$DIR/address.txt"; exit 1; fi
mkdir -p "$HOME/Library/LaunchAgents"
cat > "$PLIST" <<P
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
<key>Label</key><string>$LABEL</string>
<key>ProgramArguments</key><array><string>$PY</string><string>$DIR/serve.py</string></array>
<key>WorkingDirectory</key><string>$DIR</string>
<key>RunAtLoad</key><true/><key>KeepAlive</key><true/>
<key>StandardErrorPath</key><string>$DIR/server-error.log</string>
</dict></plist>
P
launchctl bootout "gui/$(id -u)/$LABEL" >/dev/null 2>&1
launchctl bootstrap "gui/$(id -u)" "$PLIST"
sleep 2
IP=""; for i in en0 en1 en2 en3 en4 en5; do a=$(ipconfig getifaddr $i 2>/dev/null); [ -n "$a" ] && IP="$IP $i=$a"; done
OK=$(curl -s -o /dev/null -m 5 -w "%{http_code}" "http://127.0.0.1:8788/clips/manifest.json")
FIRST=$(echo $IP | awk '{print $1}' | cut -d= -f2)
{ echo "status=$OK"; echo "addresses=$IP"; echo "python=$PY"; echo "name=$(scutil --get LocalHostName 2>/dev/null)"; date; } > "$DIR/address.txt"
echo
if [ "$OK" = "200" ]; then echo "CaptCan TV is running on this Mac."; echo "TV address:  http://$FIRST:8788/?tv"; else echo "It did not start (status $OK). Tell Claude."; fi
echo "You can close this window."
