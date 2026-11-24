# CaptCan TV and intro: where things stand (Nov 23 2026, late)

Read this first in any new chat about the store TV or the intro.

## What is live on the TV (index.html, BUILD 1123-2350a or later)
- Loop is data: `FLOW` (any day / Wednesday). Every day: reel, clip, New this week, reel, clip, reel, New this week, sign-up, reel, clip.
- Art reels: `REELS` (Doom, Absolute Batman, Midnight, Black Suit), mp4s in `v/`, scene `S.reel`.
- Clips and trailers: `CLIPS` (YouTube ids, type c/s/k, optional start `s` and end `e`), mixed order in `TRL()`, played by `YTP`. Radio dips and returns slowly.
- Remote (`#r`, PIN in localStorage): Lineup tab shows the loop, reels and clips in play order.
- A phone or laptop opens the TV link as a preview that ignores the remote. Add `?tv` to make that device act as the TV.
- Off the loop, remote only: every older screen (Hot this week, games, market, services, spotlights).

## Not verified
- YouTube clip playback (test rig cannot reach YouTube). Radio dip (cannot hear). Samsung behaviour.

## Open, in priority order
1. MAIN PROJECT: master intro, near shot-for-shot Marvel Studios replica, Blender on the Mac. Nine beats from the Spider-Man: Brand New Day intro (playlist PLr_UAhQSlwSXsb4bqnttfjZoVQxxGI8Li). Not started. Needs the real fanfare audio file (the one supplied was a fan remake). Must end on brushed-metal logo over a Captain Canada backdrop, leaf lights like neon, ".ca" pops in. Rejected so far: flat 2D versions, plain letter sides, cutting to a separate logo screen, rushed pacing, handheld shake.
2. More intro templates after the master: Batman animated style with Captain Canada, Spectacular Spider-Man newspaper style, classic 2002 page-flip, DC. Staff pick the intro from the remote.
3. Art reels are "not bad, not amazing". Known flaws: glitch on every cut, dead space on single-cover shots, scan edges and barcodes, one generic title font, flat pacing, weak logo ending, no character cutouts. Need the location of the illustrator files and cutouts.
4. Doom trailer screen built around the new Doomsday movie poster. Needs the poster file from Reilly.
5. Staff theme builder on the remote (title + search + untick books + put on TV).
6. Clips: more variety in talking clips; own reels with a "follow on Instagram" tag (needs the reel files and the handle); pair clips with matching reel and books; play clips clean and full screen (proposed, not confirmed); weight the Doomsday trailer until Dec 18 (offered).
7. Flow: six-step block proposed, waiting on Reilly. Then rebuild the remote around it.
8. Tuesday upload screens: need what is in the upload. Wednesday loop uses older, unimproved screens.
9. Fire Stick 4K Max plus a kiosk browser recommended; set up when it arrives.
10. Old logo still in the TV bar and opening screen.

## Tools in this repo
- `tools/art-reel/`: `wall2.html` (the reel engine), configs `w_*.json`, `rtv.py` (renders frames with headless Chrome). Covers come from Shopify (featured images, trimmed of white scan borders) into `bt/` next to the html.
- `tools/intro/`: `intro5.py` (2D intro cut to audio hits, options A, C=red pages, D=punch-in), `endcard.py` (neon leaf and .ca pop), `scene3.py` (first Blender attempt, rejected look), logo masks.

## Working rules learned tonight
- Replicate the reference; do not reinterpret it. Study it frame by frame first.
- No zooming into parts of covers. No minimalist editorial layouts. Titles must match the books shown.
- Do not add screens to the loop that were not asked for. Cut before adding.
- Find things first (files, links, what is installed) before asking Reilly.
- No downloading video or music; clips play from YouTube. Reilly supplies audio and any poster with actors.

## Update Nov 24, 11am (supersedes loop notes above)
- BUILD 1124-1105a. The loop is ONLY art reels + clips/trailers, in every mode (playlist() returns FLOW for all modes). Old screens (board, wall, keys, guess, join, howto) are out of the loop; still reachable from the remote "Put up now".
- Cause of "still shows screens I hate": the Fire Stick was in saved mode "sell", which ran the old per-mode playlists.
- Fire Stick (Silk, AFTKRT) confirmed on this build via relay ack, sound unlocked, Doomsday trailer playing.
- To add a screen back: add its key to FLOW.any / FLOW.wed.

## Fire Stick findings, Nov 24 ~11:15am (BUILD 1124-1112a)
- Device: Fire TV Stick 4K Max (AFTKRT, Fire OS 8, Silk 152). Reilly will not buy other hardware.
- Fire OS 8 removed app auto-start on boot. Nothing can launch the channel by itself after a full power cut. The stick sleeps rather than powering off, so Silk should return to the page on wake (untested overnight).
- Measured over the relay (ack fields pf/pv): 57-60 fps, 6 dropped frames of 400 on a reel. Hardware is fine.
- The page was NOT full screen (viewport 1546x773 in Silk with browser bar). Full screen and sound both need one OK press after every load. Every relay "reload" drops both, so do not reload during store hours.
- YouTube clips took 6 to 60s to reach ready; while waiting the loop plays another art reel (only 4 exist, so it repeats).
- Parental-controls PIN unknown to Reilly; blocks Settings changes on the stick. Reset is at amazon.com/pin signed into the account the stick is registered to.
- Reilly's verdict: loop "not approved", still not the best loop or setup. Only 4 art reels + 19 clips exist; no products, no own reels, no Tue/Wed programming.


## Takeover, Nov 24 afternoon (new chat in CaptCan 4). Read this section first; it supersedes the notes above where they differ.

### What is live on the TV
- Still `index.html` BUILD 1124-1112a. Nothing changed on the TV today. The stick was full screen with sound at 11:28am.

### Built today, waiting on Reilly's yes
- `next.html` (BUILD 1124-1445k or later): the same page with the new channel engine. Preview: https://rdjmitch.github.io/captcan-tv/next.html (a phone or laptop shows it as a preview). To make it live: `cp next.html index.html`, bump nothing else, push; the TV picks it up at the 7 to 9:30am self-update or on a reload (a reload in Silk needs one OK press after).
  - `CH` = the programmer. `BLOCKS` holds two block templates that take turns: intro, ident, reel, trailer, cartoon, product, reel, scene, talk, own / ident, reel, cartoon, scene, product, reel, trailer, cartoon, own. Kinds with no approved screens (`SCREENS.intro/ident/product/own`) are skipped, so the slots for the Marvel-style intro, idents, product screens and CaptCan's own reels already exist: add `{id,n,fn:()=>scene}` to `SCREENS.<kind>` once Reilly approves a screen.
  - Shuffle bags per kind (saved in localStorage `cctvCh`): nothing repeats until everything else of its kind has played. `LEADTR` (Doomsday final trailer) takes every other trailer slot.
  - `YTS`/`YTM` = two hidden YouTube players. ROOT CAUSE FOUND for slow or failed clips: YouTube pre-roll ads on non-official uploads (see CLIPS.md, Nov 24 check). During an ad the player state is -1 while its clock advances. The loader now treats that as "ad running, wait" (up to 100s) and calls a player ready only once the clip itself reached state 1 and is paused on its first frame. Two players can play at the same time, so the next two clips load while the TV plays and clips can run back to back. A clip not ready at its slot pulls the next non-clip screen forward or fills with one reel (max twice), then is skipped. Two failures in a row bench a clip for 10 minutes. A state -1 during live playback (mid-roll ad) ends the clip at once so no ad shows on the TV.
  - Fixed: clips with an end time past 175s were cut off (Stan Lee clip); radio no longer blips up between two back-to-back clips.
  - After a sleep of 60s or more the page drops stale players, restarts the radio and moves on.
  - Ack over the relay now carries `ch` (shown, fillers, skips, stalls, load waits, failed ids, next 8 slots), `ytp` (both players) and `app`.
  - Remote Lineup tab rewritten: the blocks, which slots are empty, every reel and clip by kind, and how often each comes back.
  - `tools/channel/patch.py <BUILD> <out>` rebuilds next.html from index.html. Once next.html is promoted, edit index.html directly and delete the patch.
- Tested: headless Chromium with a stand-in YouTube player (order, no repeats, error clip, slow clips) and the Mac's browser against real YouTube. NOT yet run on the stick.

### Fire TV app (tools/firetv-app, built to app/captcan-tv.apk by GitHub Actions)
- Finding that replaces "nothing can auto-start on Fire OS 8": an app CAN start at power-on once `adb shell cmd appops set <package> SYSTEM_ALERT_WINDOW allow` is run (ScreenCloud documents this for Fire OS 8 sticks). So the answer for the stick is the small CaptCan TV app, installed over ADB from the Mac mini. See tools/firetv-app/README.md for what it does and the exact steps.
- Blocked on Reilly: ADB debugging must be turned on in the stick's settings (behind the parental PIN he does not know; reset at amazon.com/pin).
- Never run on the device yet.

### The relay from a cloud chat
- ntfy.sh is not reachable from the cloud container. Read and send through the Mac's browser pane: open any ntfy.sh page, then `fetch("https://ntfy.sh/<topic>-ack/json?poll=1&since=30m")`. ntfy free tier is about 250 messages a day per IP, so do not add chatty logging.
- A Mac is also answering pings as a TV (a tab open with ?tv). Tell acks apart by `ua` (AFTKRT = the stick).

### Still open, in Reilly's order
1. Stick: install the app (needs his settings step), then prove clips, sound and power-on start on the device.
2. Loop: his yes on next.html, then promote. Then ident and product screens to the reel standard (show stills first).
3. More and better themed reels from live Shopify stock; needs the location of Andrew Thomas's files and cutouts.
4. Tuesday upload and Wednesday new-release programming.
5. Remote: simple everyday remote plus the drag-and-drop builder and the one view of everything (Lineup tab is the start).
- The Marvel-style intro belongs to CaptCan 6; its slot is `SCREENS.intro`.

### Update Nov 24, 12:25pm: the new channel is LIVE on the TV
- Reilly said yes. `next.html` was copied over `index.html` (BUILD 1124-1445k), the stick was reloaded over the relay (`{cmd:"reload",only:"AFT"}`) and someone pressed OK. Stick ack at 12:24: full screen, 60 fps, Doomsday trailer live, next cartoon opening ready behind it, no failures.
- From here edit `index.html` directly (`next.html` and the patch script are deleted).
- Watch `ch` in the ack: `nf` (failed loads), `ads`/`adid` (ads waited out, seconds per clip), `fi` (filler reels), `sk` (skipped clips), `stl` (stalls).

### Update Nov 24, 12:45pm (BUILD 1124-1500m, live on the stick)
- Captions forced off on every clip (`nocc`). Reel logo ending (last 3.8s of every reel file) now only plays on every 4th reel (`REELN`).
- Reilly's feedback after seeing the new channel ("not bad"), in his words, all still OPEN:
  1. It still loops the same things: only 4 reels + 18 clips + 5 trailers exist. Needs more reels and screens, not more engine.
  2. Clips are low resolution: the uploads themselves are 360p/480p fan uploads. Find official or HD uploads for each (also fixes ads).
  3. Product picks during clips and trailers must be better, rotate through several books during a clip, and sell harder. Today it is one card (the priciest match for the clip's keyword) after 14s. Show him a still before it goes live.
  4. Remote: on a computer he wants a timeline like Premiere with that kind of editing; on the phone a simple TV remote. The Lineup tab does not tell him what is playing and why.
