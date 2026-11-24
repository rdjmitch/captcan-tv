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
