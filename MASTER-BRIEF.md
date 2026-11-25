# CaptCan TV: master brief and full export

Written Wed Nov 25 2026, 2:45pm, for Reilly Mitchell. This is the one document for the shop TV. It replaces every earlier brief. Paste Part 8 into any chat or tool and it has the whole job.

---

## Part 1. What is going wrong, and why

| # | What went wrong | Why it happened | What changes |
|---|---|---|---|
| 1 | Images are weak. Reels used whatever cover scans the shop's product search returned. | Claude treated "from live Shopify stock" as the only image source and picked by title search, then by price. Neither is taste. Reilly's point: we can use ANY art, ANY way we want. | Art edits use the best art that exists for the theme: the iconic covers, textless and virgin art, posters, splash pages, CaptCan's own art. Stock scans are only for screens that sell a specific book. |
| 2 | Letter fills land on weird spots (mastheads, speech balloons, elbows). | Focal points were guessed from a small contact sheet and checked once at thumbnail size. | Every letter is placed by hand on the face or the emblem, rendered at full size, and looked at one letter at a time before anything renders as video. If a cover does not fill a letter well, pick a different image, do not force it. |
| 3 | Everything looks like one template. | One engine (letters, sliding covers, cover wall) was reused six times because it was fast. | Each theme gets its own edit built from a studied reference. No shared template. One finished piece is reviewed before a second is started. |
| 4 | Work was rushed and shipped half-checked. | Too many things in one sitting, each pushed to "done" on a desktop test, none seen on the real TV. | One piece at a time. Done means: seen full size by Claude, seen by Reilly, then seen running on the shop TV. |
| 5 | The loop lost everything that was built Nov 17 to 23. | An earlier chat cut the loop to "reels and clips only" on Nov 24, 11am, after Reilly named the screens he hated. That cut removed about 60 built screens, not just the hated six. | Restored Nov 25 (build 1125-1430a). Only the named screens stay out. Each restored screen still needs an eyes-on review. |
| 6 | The TV does not come on by itself, so staff found it "not working". | Fire OS 8 will not let any app or page start itself until one permission is granted over ADB. That needs Developer Options on the stick, which is behind a PIN Reilly does not know. The stick sat off the channel from open until 12:50pm on Nov 25 and the staff remote talked to nothing eight times. | Reset the PIN (Part 7), then the two presses, then Claude installs. Every paid signage app has the same requirement on this stick (ScreenCloud's own guide says so), so there is no shortcut app. |
| 7 | Reilly keeps having to explain and decide things he already said. | Claude asked instead of reading the record, and asked him to choose from lists he should never have to see. | Decisions come from this document. Questions to Reilly are yes/no on a finished piece, or a request for a file only he has. |
| 8 | Claude reported the TV as fine when it was not. | It read build numbers and error counts, not whether the channel was actually on screen, paused, or had trailers switched off. | Before any status report: last answer time from the TV, paused or not, full screen or not, trailers on or off, and what staff sent from the remote. |

---

## Part 2. What the TV is (Reilly's words, collected from every chat since Nov 17)

- "Our TV channel almost." Staff turn the TV on and it is on: live, fresh, fitting the day, awesome. It runs all day without him.
- Great art and cover screens with an Instagram / Pinterest feel. Covers stay big. Flat single-colour backgrounds with just the art. Cinematic Doom and black suit Spider-Man edits. Image-filled title lettering is a look he likes when it is done well.
- Current trailers (Avengers: Doomsday matters most), classic cartoon openings (Spectacular Spider-Man is the one he loves), iconic and forgotten-good movie scenes (Iron Man films, Hulk movies), short cut clips of people talking about comics and big-dollar books. Never a long talk video in full.
- CaptCan's own best reels (the Wolverine reel) with a "follow us on Instagram" tag.
- Products mixed in, but only in screens as good as the art. Product picks during clips rotate and actually sell.
- Themed, always changing, never the same few things on repeat.
- Tuesday is built around that day's upload. Wednesday is new release day: mostly that week's new releases plus the coolest screens, and it helps buyers see what is in stock, where it is and how to get it.
- The radio dips while a clip plays and comes back slowly.
- Character cutouts and CaptCan's own art (Andrew Thomas's illustrations, Captain Canada).
- His tastes: black suit Spider-Man, Red Hulk, Doom, Absolute Batman, Midnight Marvel, Wolverine.
- Staff can switch on a signing or event, pick an intro, and build their own spotlight.
- Remote: on the phone a simple TV remote. On the computer a timeline like Premiere: drag things, see every screen, the order, how often each plays.

Out, by name: Guess the Grade, Name That Book (zoomed cover game), the old Doom screen, the board / wall / keys screens, anything text-heavy, anything that looks AI-made, zoom-ins on parts of covers, minimalist editorial layouts, a theme whose books do not match its title, the same loop over and over.

---

## Part 3. Rules

1. Show the real rendered piece before it goes on the TV. Nothing new in the loop without Reilly's yes.
2. No changes land on the shop TV during store hours. Never reload it without telling him (a reload drops full screen and sound until the app is installed).
3. Claude does not rip or download video or music. Reilly supplies files. Studio clip files never go in the public repo.
4. No em dashes in anything a customer reads. Canadian spelling. CAD.
5. Never make "ask Jayden, Dad or staff" his step. No new bots, phone alerts or scheduled tasks.
6. Replicate references, do not reinterpret them.
7. A theme's images must be the theme. No near-misses.
8. Lead every update with what got done. Keep this file and HANDOFF.md current.
9. Reilly is not at the shop every day. Anything that needs hands on the stick waits for when he is, and is asked for once.

---

## Part 4. How the work is done from now on

**Pictures before building.** For each theme Claude gathers 30 to 40 candidate images from anywhere good, lays them out as one picture sheet, marks its own top 12, and sends that. Reilly strikes and adds. Only then is anything built.

**Image sources, in order of quality.** Textless and virgin cover art, key covers at full resolution, posters, splash pages, CaptCan's own art and cutouts, then product scans. Sources and any file downloads are named to Reilly first.

**Placement by eye.** Every crop, cutout and letter fill is rendered full size and checked on its own. Faces and emblems centred. No mastheads, barcodes, price boxes, balloons or scan edges inside a shape.

**One finished piece.** One edit is taken to finished, shown, and judged before the next starts.

**Judged as a channel.** The deliverable Reilly reviews is a screen recording of the real page running for ten minutes or more, not single clips.

**Better tools where they beat hand-building.**
- After Effects and Premiere on the MacBook for real edits (already installed).
- Adobe's subject cut-out for characters (connected, never used so far). The free cut-out tried on Nov 24 only worked on some covers.
- Envato templates for motion looks worth copying; Reilly thinks a subscription would earn its keep.
- Amazon's own Signage Stick is the device built for this job and starts itself. Reilly has said no more hardware, so this is recorded, not recommended.

---

## Part 5. Full export: what exists right now

**Where it lives**
- Page: `index.html` in GitHub repo `rdjmitch/captcan-tv`, branch `main`, served by GitHub Pages. captcancomics.ca/tv redirects to it. Staff remote: captcancomics.ca/tv#r.
- Live build: 1125-1430a (pushed Nov 25, 2:30pm; the stick was still on 1124-2100x at 1:08pm and picks up the new one on its next open, or 7 to 9:30am if left open).
- Notes: `HANDOFF.md` (history) and this file. Ticket: CaptCan HQ, "CaptCan TV".

**The TV**
- Fire TV Stick 4K Max (AFTKRT, Fire OS 8) in Silk. Needs one OK press after every page load for full screen and sound.
- Checked live Nov 25, 1:08pm: full screen, sound on, 59 frames a second, 9 file clips and 19 screens in 18 minutes, no failures.
- Trailers are switched off from the staff remote since Nov 24.

**The Mac mini (wired, at the shop)**
- Folder `Movies/TV/CaptCanTV`: 19 trimmed 1080p clip files, a small server that starts by itself, and "Install CaptCan TV on the stick" (one double-click installer).
- The stick moves itself to the Mac mini copy so clips play from files with no YouTube badge. If the Mac mini is off, clips fall back to YouTube.

**The app (installed on the stick Nov 25, 3:00pm; power-on start not yet proven)**
- `app/captcan-tv.apk` in the repo. Starts on power-up, full screen, sound without a press, returns by itself after Home, falls back to the internet copy.

**What the loop plays (build 1125-1430a)**
- Blocks of: one book screen, an art reel, a clip, a movie scene, one shop screen, an art reel, a trailer or clip, a talking clip. Nothing repeats until its group has played. Doomsday trailer at most every 30 minutes when trailers are on.
- Book screens: spotlights, hero book, hot this week, cover of the day, exclusives, just sold, runs, incentives, big books, trades, vote.
- Shop screens: sign-up, the app, services, pre-sales, market, about CaptCan, merch, coming soon. Wednesdays add How the site works and Hold Box. Tuesdays add the upload screen.
- Art reels: New This Week (about every 4 minutes on Wednesdays), Grails, Doom, The Amazing Spider-Man, Black Suit, Absolute Batman. Reilly rated all six a fail. They are a stopgap.
- Clips: 19 (cartoon openings, movie scenes, talking clips) plus 5 trailers on YouTube.

**Not built**
- Real art edits. Rotating product picks during clips. Own-reels screen. Idents and the intro slot content. A phone remote where every button works. The computer timeline editor. Trailers from files. A weekly automatic New This Week build. A reserved address for the Mac mini. A relay without the daily message cap.

**Not verified**
- The app on the real stick. Each restored screen on a real browser. Whether last night's and today's builds look right on the shop TV.

---

## Part 6. Order of work

1. Stick: PIN reset, two presses, install, prove on the log that power-on brings the channel up.
2. Eyes-on review of every restored screen. Cut the weak ones. Send Reilly a picture sheet of what stays.
3. One art edit, done properly: picture sheet, his picks, reference studied, built in After Effects or equal, checked letter by letter, shown finished.
4. Ten-minute recording of the whole channel for his verdict.
5. Product picks during clips. Trailers from files. Own reels.
6. Phone remote. Then the timeline editor.

---

## Part 7. What only Reilly can do

**A. The PIN (this is what blocked Developer Options).** The stick's PIN is the Amazon account's parental PIN. To reset it:
1. On the stick, when it asks for the PIN, type any wrong PIN. A reset code appears under the box.
2. On a phone or computer go to amazon.com/code and sign in with the Amazon account the stick is registered to.
3. Type the reset code, press Continue, and set a new PIN.
If no reset code appears: sign in at primevideo.com, open Account and Settings, Parental Controls, and change the PIN there.

**B. Two presses on the stick** (next time he is at the shop):
1. Settings, My Fire TV, Developer Options, ADB Debugging, On. If Developer Options is missing: My Fire TV, About, click the stick's name seven times.
2. Tell Claude "ADB is on". Claude runs the installer on the Mac mini. Press Allow when the TV asks.

**C. Files only he has:** trailer files, the Wolverine reel, the Instagram handle, where Andrew Thomas's art and cutouts are kept.

---

## Part 8. The prompt (paste this to start any chat on the TV)

```
CaptCan TV. Read MASTER-BRIEF.md in GitHub repo rdjmitch/captcan-tv before doing anything, then the top of HANDOFF.md. Everything I have asked for, every rule, what is live and what is not is in there. Do not ask me anything that is written there.

What I want: our in-store TV channel. It comes on by itself when staff turn on the TV, full screen with sound, and runs all day without me. Great art and covers shown big, current trailers, cartoon openings, movie scenes, short talking clips, our own reels, the screens we already built, and products that sell, mixed so it never feels like a loop. Tuesday is the upload, Wednesday is new releases.

How to work:
1. Images: use the best art that exists for a theme, from anywhere, any way we want. Not just our product scans. Show me a picture sheet of candidates with your top picks before you build anything. I strike and add.
2. Look at everything with your own eyes at full size. Every crop and every letter fill sits on the face or the emblem. No mastheads, barcodes or scan edges. If an image does not work, pick another.
3. No shared template. Study a real reference and replicate it. Finish ONE piece and show me before starting another.
4. Show me the channel as a 10 minute recording of the real page, not single clips.
5. Before telling me how the TV is doing, read its log: when it last answered, paused or not, full screen or not, trailers on or off, what staff sent from the remote.
6. Nothing lands on the shop TV during store hours. Nothing new in the loop without my yes. No ripping video. No em dashes. Never make "ask Jayden, Dad or staff" my step. No new bots or alerts.
7. Lead with what got done. End with done, still open, needs me. Only bring me a yes/no on a finished piece or a file only I have.

Start with Part 6 of MASTER-BRIEF.md, in order.
```
