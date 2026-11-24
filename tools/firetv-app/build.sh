#!/usr/bin/env bash
# Builds the CaptCan TV Fire TV app without Gradle. Needs the Android SDK (ANDROID_HOME) and a JDK.
# Runs in GitHub Actions (.github/workflows/firetv-app.yml); output: app/captcan-tv.apk at the repo root.
set -euo pipefail
cd "$(dirname "$0")"
VERSION="$(cat VERSION)"; CODE="${VERSION//./}"
SDK="${ANDROID_HOME:-${ANDROID_SDK_ROOT:-}}"; [ -n "$SDK" ] || { echo "ANDROID_HOME not set"; exit 1; }
BT="$SDK/build-tools/$(ls "$SDK/build-tools" | sort -V | tail -1)"
JAR="$SDK/platforms/$(ls "$SDK/platforms" | sort -V | tail -1)/android.jar"
echo "build-tools: $BT"; echo "platform: $JAR"
rm -rf build; mkdir -p build/gen build/classes build/dex
printf 'package ca.captcancomics.tv;\npublic final class BuildInfo { public static final String VERSION = "%s"; }\n' "$VERSION" > build/gen/BuildInfo.java
"$BT/aapt2" compile --dir res -o build/res.zip
"$BT/aapt2" link -o build/unsigned.apk -I "$JAR" --manifest AndroidManifest.xml \
  --min-sdk-version 22 --target-sdk-version 30 --version-code "$CODE" --version-name "$VERSION" build/res.zip
javac -source 8 -target 8 -nowarn -cp "$JAR" -d build/classes $(find src build/gen -name '*.java')
"$BT/d8" --release --min-api 22 --lib "$JAR" --output build/dex $(find build/classes -name '*.class')
(cd build/dex && zip -q ../unsigned.apk classes.dex)
"$BT/zipalign" -f 4 build/unsigned.apk build/aligned.apk
# Signed with a one-off key made during the build (no key is stored anywhere). Because the key changes with
# every build, installing a newer build means removing the old app first; install.sh does that for you.
KP="once$(date +%s)$RANDOM"
keytool -genkeypair -keystore build/once.keystore -storepass "$KP" -alias tv -keyalg RSA -keysize 2048 -validity 12000 \
  -dname "CN=CaptCan TV, O=CaptCan Comics, L=Brantford, ST=Ontario, C=CA" -storetype PKCS12 2>/dev/null
"$BT/apksigner" sign --ks build/once.keystore --ks-pass "pass:$KP" --ks-key-alias tv --out build/captcan-tv.apk build/aligned.apk
"$BT/apksigner" verify --print-certs build/captcan-tv.apk | head -3
mkdir -p ../../app; cp build/captcan-tv.apk ../../app/captcan-tv.apk; ls -la ../../app
