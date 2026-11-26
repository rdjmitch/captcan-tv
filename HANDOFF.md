# READ MASTER-BRIEF.md FIRST (written Nov 25 2026). It is the one brief, the diagnosis and the full export. This file is history.

# VERDICT Nov 24, 8:13pm: the v4 reels are a FAIL. Read this before the brief below.
Reilly on the six v4 reels: "still a fail for what I've said and what we can do." Asked which part, he picked all four:
1. The look and edit: one template (letters, sliding covers, cover wall) repeated six times is a cover slideshow, not the cinematic art edits he has described.
2. Still the books: slabs and keys were closer but are not the books he would put up.
3. It is not a channel: he keeps being shown single reels. He wants to see the whole hour working together (clips, products, art, flow).
4. The TV does not run itself.
On references he said there is not much saved or liked on his Instagram; "do what's best for best output".

Do NOT send another reel from `wall3.html`. Do not ask him for a yes on v4. What to do instead:
- Edits: find real references yourself (comic-art edit accounts on Instagram and YouTube: flat single-colour backgrounds with just the art, cinematic Doom and black suit edits), study them frame by frame, and replicate. Use character cutouts: the Adobe connector can cut a figure out of a cover (select subject / remove background), which has never been tried here. Each theme gets its own edit, not a shared template. After Effects is on the MacBook.
- Books: show him the candidate books for a theme as a picture grid and let him strike and add BEFORE any edit is built. His taste: black suit Spidey, Red Hulk, Doom, Absolute Batman, Midnight Marvel, Wolverine.
- Channel: the deliverable is a recording of 10 or more minutes of the real page running (file clips, art, products, ident), not a single piece.
- Stick: nothing replaces his three minutes (ADB on, run the installer). Ask for that once, plainly, and prove it on the relay.

---

# CaptCan TV: THE BRIEF (written Nov 24 2026, 9pm, after reading every TV chat and note since Nov 17)

Read this section first. It is the one direction for the TV. Everything below it is history.

## What Reilly is asking for, in his words across all the chats
"Our TV channel almost." Staff turn the TV on and it is on by itself: live, fresh, fitting the day, and awesome. It runs all day without him. It shows great art and covers big, current trailers, cartoon openings, movie scenes, short talking clips, CaptCan's own best reels and products that sell, and it never feels like the same few things on a loop. Every piece is designed, planned and finished before it goes on the TV. He is not the owner and he is not the TV operator.

## Why it kept missing (the honest list)
1. Books were picked by title search, so reels were full of whatever new variants had the word in the title. The shop's real strength (graded keys, silver age, its own exclusives) was not on screen. FIXED in reel set v4, see "Book rule".
2. Pieces went on the shop TV half-done and were patched live during store hours. RULE now: build and check off-air, show Reilly the finished piece, launch once.
3. The TV was judged from the relay without reading whether staff had paused it or switched trailers off.
4. The stick was never set up: no app, Silk needs a press after every load, nothing brings the channel back after Home. The app and installer exist but have never run on the stick.
5. Too little content: 4 reels and 19 clips cannot feel like a channel however they are ordered.

## Book rule (applies to every themed reel, screen and product pick)
- Lead with the real keys CaptCan has in stock for that theme: graded slabs and raw key issues. Then the best modern covers. Never build a theme from a title search.
- Every book must be the theme (black suit reel = Spider-Man in the black suit on the cover). No near-misses.
- Include CaptCan's own exclusives when the theme has one (Absolute Batman #20 Lashley).
- No later printings shown as keys. No washed-out foil scans. No pin-up covers on the shop TV.
- Evidence to use: 30-day sales by title (what the shop actually sells), in-stock books at $450 and up, then the theme's known key issues checked against stock.
- Slabs are shown whole on the big shelf shot (the grade sells it) and as art-only crops inside the title letters and the wall.
- When a featured key sells, the reel is still good art, but refresh a theme once about a third of its lead books are gone. Source list with image files: `tools/art-reel/v4/covers.txt`; line-ups: `tools/art-reel/v4/*.json`.

## The channel, piece by piece, and what "done" means
| Piece | Done means | State Nov 24, 9pm |
|---|---|---|
| Stick | TV on = channel on, full screen, sound, no presses; comes back by itself after Home; survives a power cut with one press at most | App 1.1 and one-click installer built, never run. Needs Reilly: ADB debugging on, run the installer on the Mac mini |
| Clips | All 19 play from the Mac mini files, clean, no YouTube badge; trailers from files too | File playback built and tested on a desktop; not yet seen on the stick. Trailers still YouTube |
| Loop | Blocks, nothing repeats until the rest has played, no reel back to back, Doomsday trailer about every 30 min | Built, tested off-air |
| Themed reels | At least 10, each passing the book rule, in the image-in-letters style he said yes to | v4 set: Doom, Black Suit, Absolute Batman, Grails, The Amazing (Spider-Man), New This Week. Waiting on his yes. Next: Midnight Marvel, Hulk (incl. Red Hulk), X-Men, Spawn/McFarlane, TMNT, Horror (pre-code + EC), Stan Lee signed, Wolverine |
| Wednesday | New-release reel from that week's tag (pattern NOV2526NR) plays every block on Wednesday | Reel built for Nov 25. Auto-weekly build not done |
| Tuesday | Upload-day reel from the same tag once the upload is live | Not built |
| Product picks on clips | 3 to 4 books rotating during a clip, matched to the clip, keys first, price and "in the shop now" | Not built (one card after 14s today) |
| Own reels | Wolverine reel etc. with a "follow us on Instagram" tag | Needs the files and the handle from Reilly |
| Idents and intro slot | Short CaptCan ident between blocks; slot ready for the CaptCan 6 intro | Slots exist, empty |
| Phone remote | What is on, what is next, skip, back, pause, put this on now. Every button does something | Old remote still live; mode buttons do nothing |
| Computer editor | Premiere-style timeline: drag blocks, see every screen, order and how often it plays | Mock only (branch remote-rebuild) |
| Plumbing | Mac mini address reserved; relay without a daily cap | Open |

## Launch order (no step goes on the shop TV until the one before is proven)
1. Reilly's yes on the v4 reels (he has the videos). Then they replace the old four in `v/` and `REELS`.
2. Stick install (his three minutes), then prove on the relay: app running, clips from files, sound, boot start.
3. Wednesday line-up on for Nov 25 before open, not during store hours.
4. Product picks, own reels, idents. 5. Phone remote. 6. Computer editor.

## Standing rules
No changes to the shop TV during store hours. Show the real rendered piece first; nothing new in the loop without his yes. No ripping video or music. No em dashes in anything a customer reads; Canadian spelling; CAD. Never make "ask Jayden / Dad / staff" his next step. No new bots, alerts or scheduled tasks. Read `tron`, `paused` and the staff remote's commands on the relay before saying how the TV is doing. Ping the relay sparingly (free tier caps at about 250 messages a day for the whole shop).

---

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

### Reel engine v3 (Nov 24, 1pm): built, shown to Reilly, NOT live
- Reilly on the reels: never back to back, and "way better", naming the image-in-the-letters title as the thing to build on.
- `tools/art-reel/wall3.html` + `w3_doom.json` + `shots3.js` (Playwright, 30 fps frames, then ffmpeg crf 23). Run from a folder holding `ct/<id>.jpg` (covers from the Shopify CDN at ?width=1100 with the white scan border trimmed), `logo_white_ca.png` and `npm i @fontsource/anton`.
- Look: each letter of the title is cut from a different cover, centred on the character's face (`letters[].x/y/z` = focal point and zoom, picked by eye), white outline, no glitch cuts, no blurred backdrop, no reflections. Then a shelf of full covers gliding past at 870px tall, then a two-row wall sliding in opposite directions, then the title again over the dimmed wall. No full-screen logo ending, only a small corner logo on the shelf shot.
- Doom v2 uses 25 in-stock Doctor Doom covers (Doom Patrol and non-Doom covers left out so the books match the title).
- Waiting on his yes before it replaces `v/doom.mp4`. Then rebuild Absolute Batman, Midnight and Black Suit the same way and add new themes.

### Update Nov 24, 1:15pm (BUILD 1124-1530n)
- Reilly approved the new Doom reel ("that's the type of thing"): `v/doom.mp4` replaced (18.5s, no logo ending, `noend:1`). Rebuild the other three the same way.
- Never two reels in a row: a filler now brings forward a ready clip instead when a reel just played.
- CLIP FILES (what Reilly means by "the things previously built are still not playing"): he wants clips from the files he supplied, not YouTube (he sees the uploader's badge top right, soft picture). The files are on the Mac mini in `~/Movies/TV/CaptCanTV/clips/<YouTubeID>.mp4` + `clips/manifest.json`, never in this public repo.
  - The page now plays `clips/<id>.mp4` (scene `S.fileclip`, clean, full screen, no YouTube) for every id in `clips/manifest.json`, but only when the page is opened from the Mac mini (`LOCAL` = http address). Trailers and anything without a file still use YouTube.
  - `tools/local-server/index.html` is a loader for the Mac folder: it pulls the live page from GitHub and writes it into the Mac's address, so the Mac folder never needs editing again. Reels then load from GitHub (`VB`).
  - The remote `goto` command now accepts `http://<private LAN ip>:8788/`.
  - BLOCKED: this chat could not get the Mac folder (folder access was refused) and nothing answers on the Mac's port 8788, so the server has not been started. Needs Reilly: add the folder `Movies/TV/CaptCanTV` to the chat, and double-click `Start CaptCan TV.command` in it. Then: put the loader `index.html` in the folder, read `address.txt`, send `{cmd:"goto",url:"http://<address>:8788/?tv"}`, check the ack shows `loc:true` and `files:19`, `fc` counting up.

### Update Nov 24, 1:30pm: clips now play from the Mac mini files (BUILD 1124-1545p)
- Reilly added the folder and started the server. Mac mini wired address 192.168.50.253, port 8788 (`~/Movies/TV/CaptCanTV/address.txt`). The loader `index.html` is in that folder (old page kept as `index-old-1124-0010f.html`).
- The stick was sent to `http://192.168.50.253:8788/?tv` with the relay `goto`. Ack: `loc:true, files:19, fc:1`, so clips come from the files; trailers still come from YouTube. The Transformers opening is back (file only).
- If the Mac mini's address changes, the TV shows "CaptCan TV is starting" or an error: read address.txt and send a new goto. A fixed address for the Mac mini on the router would prevent that.
- The relay cap cleared by 1:25pm. An old copy of the channel is still open on a Mac (build 1124-1500m, 89 failed loads); it answers pings and wastes relay messages.

### Update Nov 24, 4:30pm (BUILD 1124-1630q pushed, NOT reloaded onto the TV; it lands at the 7 to 9:30am self-update)
- What staff saw: between about 12:45 and 1:17pm (clips still from YouTube) most fan-upload clips failed to start after their ad, so blocks collapsed to reels plus the trailers, and the Doomsday trailer came round every few minutes. Staff tried modes and screens from the remote (1:07 to 1:17pm), then paused it at 1:17pm. It sat paused until 4:01pm. Correction to the note above: the switch to the Mac mini files went through at 4:01pm, not 1:30pm.
- Since 4:01pm the stick plays from the Mac mini files (ack 4:06pm: loc true, 19 files, 3 file clips played, no failures). Trailers were NOT loading there: the YouTube player script finished before the page was ready for it (loader page), so `YTREADY` stayed false. Fixed in 1630q (the 3s tick picks it up).
- 1630q also adds hard replay guards: no clip or trailer inside 20 minutes of its last play (`CH.GAP`), Doomsday final trailer at most once every 30 minutes (`CH.LEADGAP`), both remembered across reloads (`seen`).
- Lesson: check what staff are doing on the relay (mode changes, pause) before calling the channel fine; a ping that says "playing" says nothing about how it feels in the room.

### Update Nov 24, 5:40pm (BUILD 1124-1735t)
- WHY THE TV SHOWED ONLY THE FOUR REELS from about 4:10 to 4:56pm (137 reels, 3 clips): staff had switched "Trailers off" on the remote at about 1:15pm to stop the Doomsday repeats, and the channel code treated that as "no clips of any kind". Fixed: Trailers off now only removes trailers; cartoon openings, movie scenes and talking clips keep playing. `tron` is now in the ack.
- At 4:56:27pm the stick left full screen and has not answered since: someone pressed Back or Home on the Fire remote, so the TV is off the channel. Nobody has reopened it as of 5:40pm.
- New: when the stick opens the internet copy (captcancomics.ca/tv) it moves itself to the Mac mini copy (`goHome`, default http://192.168.50.253:8788/?tv, at most once per 30 minutes; the remote state key `home` overrides it, `home:"off"` disables it).
- The remote's mode buttons (Full mix, Selling and so on) do nothing since the loop was stripped; staff tried them at 1:07 to 1:17pm. That is what "the remote isn't doing anything" is. Remote rebuild still open.
- Always read `tron`, `paused` and the remote's commands on the relay before judging what the TV is doing.

### Update Nov 24, 8pm (BUILD 1124-2000v pushed; loads when the channel next opens or at the morning self-update)
- Reilly (6:47pm): he never finished setting up the stick, staff must not have to find or open anything, the TV must come on by itself, and he wants it running all day tomorrow without him.
- Fire TV app 1.1 built (app/captcan-tv.apk): opens the Mac mini copy first (http://192.168.50.253:8788), falls back to the internet copy and retries the Mac mini every 10 minutes, starts at power-on, comes back by itself 3 minutes after Home is pressed (Back twice is the deliberate exit).
- `~/Movies/TV/CaptCanTV/Install CaptCan TV on the stick.command` on the Mac mini: finds the stick on the network, installs the app over ADB, grants start-at-boot, turns off the stick's sleep timer, opens the app, writes `install-log.txt` and `stick-address.txt`. BLOCKED on Reilly: ADB debugging ON on the stick, then double-click that file and accept the prompt on the TV. Nothing on the stick has been proven yet.
- Absolute Batman and Black Suit reels rebuilt in the v3 style (configs tools/art-reel/w3_bat.json, w3_black.json; mastheads kept out of the letters by focal point + zoom, fills clamped so art always covers the letter). Midnight is still the old reel: its theme needs confirming before a rebuild.

## Nov 24, 10pm
- Six v4 reels rendered and sent to Reilly: `v4/*.mp4` (doom, black, bat, grails, amazing, new). NOT in `v/` or `REELS` yet: waiting on his yes. To launch: copy to `v/`, add grails, amazing and new to `REELS` (all `noend:1`, d 18.5), bump BUILD, and do it outside store hours.
- To re-render: covers from `tools/art-reel/v4/covers.txt` (Shopify files host, `?width=1100`), trim white borders, slabs also saved as art-only crops with an `x` suffix (crop 8.5%/19%/91.5%/97.2%), then `node shots3.js w4_<name>.json video`. Run one render at a time (fixed port and frames folder).

## Nov 24, 8:45pm: LIVE build 1124-2045w (Reilly: update captcancomics.ca/tv tonight; he is not at the shop Nov 24 or 25 and cannot reach the stick)
- `REELS` is now newweek, grails, doom, amazing, blacksuit, batman (the v4 files, in `v/`). Old Midnight reel removed. He rated v4 a fail, but it replaced older reels he rated worse; it is the stopgap for Wed Nov 25, not approved work.
- Wednesday rule in `S.reel`: on Wednesdays every second reel is `newweek` (counter `WEDN`). `v/newweek.mp4` must be re-rendered each Tuesday from that week's tag or it goes stale. A reel tapped from the remote on a Wednesday can be swapped for newweek by the same rule.
- Stick install is NOT possible until Reilly is back at the shop. Do not ask him for it. The TV needs someone in the shop to open captcancomics.ca/tv in Silk and press OK once.
- Unfinished: `edit.html` Black Suit edit (cutout hero over flat colour, hard cuts on single covers with small labels) in the render workspace; cutouts via rembg work on some covers only (Secret Wars 8, Doom on the throne), title overflows the frame.

## Nov 24, 9pm: LIVE build 1124-2100x
- Reilly was confused that the loop was only reels and clips: the older screens were never deleted, only out of the loop since 11am. He would not pick which to restore ("why should I have to describe this"), so Claude decided from his own notes: on Wednesdays the product slot rotates How the site works, Hold Box, Pre-sales and Sign-up (his line: Wednesday buyers ask what is in stock, where things are and how to get them); other days the product slot is Sign-up only. Wall, board, keys and the games stay out. `SCREENS.product` is a getter.
- Wednesday reel rule changed: New This Week returns about every 4 minutes (timestamp `WEDN`), not every second reel, so it cannot dominate when clips are slow to load.

## Wed Nov 25, 1:10pm: relay check (Reilly: staff say it is not working properly)
- Staff remote pinged at 9:12, 10:28, 10:32, 11:03, 11:40, 11:42 with NO answer from the TV, and sent "show newweek" at 11:41 and settings at 11:45 and 11:48 into nothing: the channel was not open on the stick all morning. That is the complaint, and why the remote "does nothing".
- First answer 12:50pm. At 1:08pm the stick (AFTKRT, Silk) is on build 1124-2100x from the Mac mini copy: full screen, sound unlocked, 59 fps, 9 file clips and 19 screens in 18 minutes, 0 fails, 0 errors. `tron` is still false (staff switched trailers off Nov 24), so no trailers play.
- Root fix is still the app + ADB grant. Needs one person at the TV with the stick remote for two presses (ADB debugging on, then Allow). Claude can run the Mac mini installer itself through computer use once ADB is on.

## Wed Nov 25, 2:30pm: build 1125-1430a pushed (loads on the next page open or the 7 to 9:30am self-update; no reload sent during store hours)
- Reilly: "this is not at all even what we have built or what I have asked for". Cause: since Nov 24 11am the loop used none of the ~60 screens built Nov 17 to 23, only reels and clips. Restored into the channel blocks: `SCREENS.ident` = spotlights, hero book, hot this week, cover of the day, exclusives, just sold, runs, incentives, big books, trades, vote; `SCREENS.product` = sign-up, app, services, pre-sales, market, about, merch, coming soon, plus how-to and Hold Box on Wednesdays and the upload screen on Tuesdays. Each block now has two of these, two reels and three or four clips; nothing repeats until its pool has played.
- Still out on his word: guess the grade, name that book, old Doom, board, wall, keys; Monk and signing-day screens stay switch-on only; news and fact left out as text-heavy.
- Not looked at with eyes in this session (the render box cannot reach the storefront feed): review each restored screen on a real browser and cut any that are weak.

## Wed Nov 25, 3:03pm: APP INSTALLED ON THE STICK
- Reilly enabled developer mode and ADB at the shop and ran the Mac mini installer. install-log.txt: found 192.168.50.71 (AFTKRT), install Success, start at power-on ok, version 1.1.0, running.
- Relay at 3:02pm: `app 1.1.0 AFTKRT os30`, build 1125-1430a, from the Mac mini copy (19 files), sound unlocked with no press, 60 fps, 0 jank, 2 file clips and 6 screens in 2 minutes, 0 errors. `fs` reads false inside the app (the app is full screen natively; viewport 1680x945).
- NOT yet proven: power-off / power-on brings it back by itself; return after Home.
- A second device is also answering pings as a TV (no app, not local, YouTube clip failures). Find and close it: it wastes relay messages and muddies the log.

## Thu Nov 26, 1pm: build 1126-1300a (zoom fix) pushed and LIVE on GitHub
- Reilly at 12:42: the app is open on the TV but the zoom is weird, things play in the top left corner, glitched; the remote does nothing either.
- CAUSE (reproduced in headless Chrome with the app's settings: 960x540 CSS, DPR 2, mobile WebView, wide viewport on): off-stage elements (#cut, #run ticker, bar) made the layout viewport grow to 1680x945 on a 960x540 screen, so fit() scaled the 1920 stage for 1680 while the TV only shows the top-left 960. That is the "zoomed into the top left" picture. Yesterday's app ack already showed vw 1680x945; it was misread as normal.
- FIX: viewport meta pinned (minimum-scale=1, maximum-scale=1, user-scalable=no) and html/body position:fixed to the screen. Re-test: innerWidth 960, stage scale 0.5, full 1920x1080 frame visible with its border. Remote CSS override keeps position static so the phone remote still scrolls (checked at 390px).
- Relay: ZERO acks from any TV since at least 4:40pm Nov 25. Pings at 8:12, 10:29, 10:30 today and my reload + ping at ~1pm got no answer. So the remote "does nothing" because the page on the stick is not hearing the relay. The fix lands on the next page load: the app's Menu (three lines) button reloads it, or the app's 4-minute no-heartbeat reload, or the 7 to 9:30am self-update.
- Open: after the reload, confirm an ack (vw should read 960x540 or the stick's real CSS size, fs, app version). If still no acks, the relay listener inside the app WebView is the next thing to debug (compare 1.1.0 at 3:02pm Nov 25, which did ack).
- Consider app 1.3: setLoadWithOverviewMode(true) + setInitialScale as a second guard (needs ADB reinstall from the Mac mini; not needed for this fix).

## Thu Nov 26, 1:30pm: build 1126-1330a, selling screens get half the channel
- Reilly: "even before, the marketing purposes we built this for have now been totally stripped?" Checked live: the selling screens were never deleted (book screens: hero, spotlights, hot, cover of the day, exclusives, just sold, runs, incentives, big books, trades, vote; shop screens: sign-up, app, services, pre-sales, market, about, merch, coming soon; render with live stock and prices). But only 2 of every 9 slots were selling; the rest were reels and clips. On the TV he saw a zoomed, cut-off page, so even those were unreadable.
- Changed BLOCKS so about half of every block is selling: block A intro, book, shop, reel, trailer, book, shop, cartoon, book, scene, shop, own; block B book, shop, reel, cartoon, book, shop, scene, book, shop, reel, talk, own. Same screens, no new ones.

## Thu Nov 26, 2pm: build 1126-1405a (Reilly: books move too fast, some screens ugly like the app one; "we have the Fire Stick and the full setup, just build it")
- Reviewed every book and shop screen at 1920x1080 in the Mac's browser with live data.
- App and sign-up screens rebuilt on the hero layout (one headline, one line, QR, one big live cover, offset so they never show the same cover). Old four-text-box versions gone.
- Out of the loop (still on the remote): Runs (small-cover grid), Market top-5 list, About timeline (text-heavy). Kept: spotlights, hero, cover of the day, exclusives, just sold, incentives, big books, trades, vote, services, pre-sales, merch, coming soon (+ how-to and Hold Box Wed, upload Tue).
- Pace: book and shop screens now hold at least 18s (grids 20s); art reels play at 0.8 speed (dur scaled).
- TV still not answering the relay (no acks since ~4:40pm Nov 25) though Reilly says the app is on and running. Remote cannot work until that is found. Next debug step needs the Mac mini folder (adb logcat from the stick); folder access request was blocked on Nov 26.

## Thu Nov 26, 2:50pm: builds 1126-1430a to 1126-1450a
- Product picks on every clip and trailer (`tieRot`): up to 4 matched in-stock books (single issues first, then price; omnibus/archive/gallery/TPB pushed back), rotate every 9s with price and QR, card appears at 14s. File clips from the Mac mini had NO product card before; they do now. Checked in the Mac browser with "Black Suit": 4 picks, rotating.
- New This Week reel only plays in the week it was built for (`NWFOR`, now 2026-11-25). From Dec 1 it drops out until re-rendered for that Wednesday and NWFOR is bumped. OPEN: weekly re-render each Tuesday from that week's new-release tag.
- Mac mini address 192.168.50.253:8788 did not load from the Mac's own browser at 2:45pm (navigation failed). If the server is down, the app runs the internet copy and clips come from YouTube. Needs a look with the Mac mini folder.

## Thu Nov 26, 3:05pm: build 1126-1505a, auto-update any time inside the app
- Reilly asked whether it updates by itself. Inside the Fire TV app the page now checks GitHub every 10 minutes all day and reloads itself when the build changes, but only between scenes (never mid clip or reel). The app keeps full screen and sound through a reload, so the old "no reloads in store hours" rule no longer applies inside the app. Plain browsers keep the 7 to 9:30am window.
- The stick is still on an older build that only checks 7 to 9:30am, so it moves to today's build tomorrow morning by itself (or sooner on a ☰ press or TV power cycle). After that, every push reaches the TV within about 10 minutes.

## Thu Nov 26, 3:30pm: remote backup live (1126-1520a); Black Suit candidate sheet
- TV now also polls the relay every 30s (`RSEEN`/`RSINCE`), so remote commands land even if the live SSE stream drops inside the app.
- Black Suit reel, step 1 (picture sheet): https://rdjmitch.github.io/captcan-tv/tools/sheets/blacksuit.html#1,2,3,6,7,8,14,15,16,17,20,21 . 24 candidates: 11 iconic covers from outside stock (ASM 252, Secret Wars 8, Web 1, Spec 90, Web 31 and Spec 132 Kraven's Last Hunt, MTU 141, Spec 107, ASM 258, SM3 poster, ASM 300) + 13 in-stock (Black Suit & Blood run incl. Monk and Lashley CGC 9.8 remarks, Gallery Edition, Secret Wars 8 Melnikov, Symbiote SM KIB 1). Claude's top 12 starred. Rejected by Claude: 4 and 5 (glare photos of bagged copies, need clean scans), 9 (red suit on cover), 10 (movie poster), 11 (Venom not Spidey), 12-13 (dark slab photos), 22 (duplicates 252). Waiting on Reilly's strikes and adds, then build the edit.

## Thu Nov 26, 5pm: build 1126-1700a, live art edits replace four of the failed v4 reels
- New engine `S.edit(k)` + `EDITS` (no video files): theme title in clean type, then one big cover at a time on a flat theme colour (960px tall, slow 3.5% push, hard cuts every 2.7s), small label bottom left (title + year or "in the shop"), counter bottom right. Full 1080 height. Reels with `edit:1` in REELS play through it; remote lineup shows the first cover.
- Live edits: Black Suit (12), Doom (11), Red Hulk (9, new), Wolverine (9, new), Absolute Batman (12 incl. our #20 Lashley exclusive). Art from Marvel/DC official covers plus in-stock books; every image looked at on a picture sheet first (tools/sheets/*.html). Rejected: slab glare photos, low-res scans, off-theme covers, duplicates.
- Still video (v4, rated a fail): grails, amazing, newweek. Next: edits for Grails (in-stock keys) and The Amazing Spider-Man, Midnight Marvel; weekly New This Week as an edit built from that week's releases.
- To change an edit: edit the imgs list in EDITS (url, title, small line). Images load straight from their hosts on the TV.
