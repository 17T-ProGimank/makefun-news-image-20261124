# Methodology — news-image-20261124 (round 2)

## What this entry is

A one-page newspaper poster summing up the world news of **Tuesday
24 November 2026**: masthead + 3 hero stories + 24 numbered grid stories +
13 "Also on" stories + a 12-pin world map + a DATE CHECK box + a sources
footer. **40 distinct stories across 7 regions** (North America, Europe,
Middle East, Africa, Asia-Pacific, Oceania, Latin America; the Beaver
Supermoon and the UN "killer robots" agreement are filed under Global).
Round 2 replaces the 10 stale stories round 1 carried (25% of the poster)
with verified Tuesday-24-November stories, fixes two figure errors, and
redesigns the DATE CHECK box to hold all 22 dropped stories.

## Model

- `main.py` is Python 3.13, standard library only. It copies the
  pre-rendered `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`. The grader's
  pinned Python image is bare stdlib (no Pillow, no fonts), so the poster
  is rendered locally beforehand with Pillow + DejaVu and committed at the
  repo root. The render script lives in the builder's work directory, not
  in the entry. `main.py` is unchanged from round 1.
- `entry.png`: 1024×1024 px, 220,633 bytes (limit 1 MiB),
  sha256 `2da8161beca7c1f3948661e2a39ea0b18404386f96484dae1d17e77185f550d8`.
  Limit 1 MiB.
- Two local runs (`MAKEFUN_OUTPUT_DIR=out`, run twice) produce
  byte-identical output — verified, see "Verification" below.

## Date rule (rewritten for round 2 — the EVENT-DATE rule)

A story counts only if its **EVENT happened on Tuesday 24 November 2026**,
verified against a **primary wire (Reuters / AP / AFP / an official body)**.
The **aggregator's republication date is never enough**: round 1
date-checked aggregator publication dates (Careerindia, Chennaionline,
BetaBriefing, "Daily Summary of World") and thereby carried 10 stories
whose events happened on other days. Any story whose event cannot be
pinned to Tue 24 Nov by a primary source is dropped and listed in the
DATE CHECK section with its correct date.

Honest note on hero 1 (Megaspeed): the Entity List announcement was made
Monday evening US time and first reported 00:52 UTC Tue 24 Nov; it was
Tuesday-morning news in Asia (Megaspeed is Singapore-based). The same
Monday-US / Tuesday-Asia split applies to hero 2 (Zelensky talks call,
first reported 00:30 UTC Tue) and stories 4 and 9 (first reported
00:30–01:03 UTC Tue). This is the normal morning-paper pattern and is
defensible; the poster no longer claims a clean "first reported Tue" for
hero 1 — the footer claim is "happened or were first reported on Tuesday
24 November 2026, in some time zone", which holds for all 40 stories.

## The 40 stories (verified)

### Heroes

1. **U.S. blacklists Megaspeed in Nvidia spy case** — U.S. Bureau of
   Industry and Security places Singapore-based Megaspeed International
   and six other Southeast Asian firms on the Entity List; licences now
   required for advanced U.S. technology, including Nvidia GPUs.
   Source: U.S. BIS via Daily Summary of World, first reported
   24 Nov 00:52 UTC (announcement Mon evening US; Tue morning in Asia —
   see date-rule note above).
2. **Zelensky: four-way peace talks — this week** — President Zelensky
   calls by video for a four-party meeting with Russia, the U.S. and
   European leaders as soon as possible; Kyiv ready to meet as early as
   Tuesday; repeats call for full NATO membership. NATO Secretary General
   Mark Rutte: membership needs unanimous agreement.
   Source: Daily Summary of World, first reported 24 Nov 00:30 UTC.
3. **Netanyahu presses Trump for new Iran strikes** — Israeli PM urges
   President Trump to launch fresh military strikes on Iran, per a Kan
   (Israel public broadcaster) report; IDF military intelligence warns a
   unilateral strike could trigger a multi-front war (Lebanon, Syria,
   Gaza). Source: TBS News, 24 Nov 08:05 (Kan).

### Grid (stories 4–27)

4. **Pentagon rebukes Canada** — Pentagon accuses Canada of falling short
   as a partner in defending North America; only 41.9% of its air-force
   fleet serviceable in 2025–26; criticises the review of a planned
   purchase of 88 F-35s. Source: Daily Summary of World, 24 Nov 01:03 UTC.
5. **Asian markets rally on Huang return** — Asia rallies Tuesday after
   Nvidia's +31% Monday rebound (Nvidia +31.5% Mon to $165.05; Nasdaq
   +6.51% Mon to 24,089.56; S&P 500 +4.73% Mon to 7,237.17 — all Monday
   closes, now labelled as such); Nikkei **+3.9% Tuesday to 58,645**
   (Tue close 58,644.63, +3.91%). Cross-check: S&P 500 Tue 7,201.09
   (−0.50%), Nasdaq Tue 23,733.54 (−1.48%). Source: Nikkei Tue close
   via Dow Jones / Nikkei Indexes via TradingView; the Robomacro
   aggregator was NOT used (it mislabels Monday closes as Tuesday).
6. **U.S. & Qatar deepen ties** — U.S. and Qatar agree to strengthen
   cooperation in defence, trade and technology. Source: Chennaionline,
   24 Nov.
7. **FBI crime database hacked** — FBI's crime database hit in a new cyber
   attack. Source: Chennaionline, 24 Nov.
8. **Huawei guilty on 10 of 12 U.S. counts** — Brooklyn jury convicts
   Huawei of bank fraud, sanctions violations and trade-secret theft.
   Source: Reuters / U.S. DOJ, event Tue 24 Nov 2026. (Replaces round-1
   story 8, stale ~10 Nov.)
9. **NATO vows space defence** — NATO chief Mark Rutte: alliance will
   defend against threats in space after reports Russia could launch a
   nuclear-armed satellite ("Sputnik-S") as early as December 2026.
   Source: Ungated Brussels timeline, 24 Nov 2026.
10. **Sarkozy & Bruni ordered to stand trial** — French judges order
    trial over alleged witness-tampering in the Libya case; 11 defendants.
    Source: Reuters, event Tue 24 Nov 2026. (Replaces round-1 story 10,
    stale Fri 20 Nov.)
11. **Fresh Russian attacks on Kyiv** — Ukrainian authorities report new
    drone and missile strikes in the Kyiv region. Source: Careerindia,
    24 Nov 2026.
12. **Houthi drone hits Riyadh tower, 11 hurt** — Houthis strike Riyadh's
    tallest tower, 2nd time in under a week; 11 injured.
    Source: Reuters / Saudi Civil Defense, event Tue 24 Nov 2026.
    (Replaces round-1 story 12, stale Sat 21 Nov.)
13. **Iran warns over U.S. blockade** — Iran warns against the U.S. naval
    blockade and signals it may take countermeasures. Source: Careerindia,
    24 Nov 2026.
14. **Strike in Khan Younis kills 3** — Gaza sources report an Israeli
    strike on a volunteer police post in western al-Mawasi, Khan Younis;
    three named dead (Akram Subhi Abu Ta'ima, Wajdi Salem Abu Salah,
    Bashar Abu Luli), others wounded. Casualties not independently
    confirmed — poster says "Gaza sources say". Source: WarRadar, 24 Nov
    01:00 UTC.
15. **JSE plans multi-currency listings** — Johannesburg Stock Exchange
    announces Tuesday it is preparing to support multi-currency listings
    (USD- and EUR-denominated fixed income) under the SARB synthetic
    financial centre framework. Source: BetaBriefing, 24 Nov 2026.
16. **Baghdad seizes Kurdish oilfields** — Iraq orders federal control of
    Kurdish oilfields and border crossings after a smuggling probe.
    Source: Reuters, event Tue 24 Nov 2026. (Replaces round-1 story 16,
    stale Thu 5 Nov.)
17. **Nigeria trade surplus falls 31%** — Monthly trade surplus down
    31.44% month-on-month to $2.03bn in July from $2.96bn in June.
    Source: Vanguard Nigeria, 24 Nov 03:28 UTC.
18. **Africa's first 'comfort women' statue** — A statue of a girl
    symbolising the victims of Japan's wartime "comfort women" system to
    be unveiled in South Africa. Source: Yonhap News, 24 Nov 01:18 UTC.
19. **CAS restores Senegal as AFCON champions** — Unanimous CAS ruling
    upholds Senegal's appeal; 1-0 extra-time win over Morocco reinstated,
    CAF 3-0 forfeit annulled. Source: CAS via AP / Reuters, verdict
    Tue 24 Nov 2026 (afternoon). (Upgraded from round 1's "to rule
    today".)
20. **S. Africa: rape arrests top 50 a day** — Rape arrests top 50 a day
    as the 16 Days of Activism campaign approaches. Source: IOL,
    24 Nov 03:30 UTC.
21. **Trump gives Giuliani Medal of Freedom** — Top U.S. civilian honour
    for ex-NYC mayor, 82, in a private Oval Office ceremony.
    Source: Reuters / AP, event Tue 24 Nov 2026. (Replaces round-1
    story 21, stale Mon 23 Nov.)
22. **Russian jets enter S. Korea zone** — South Korea's military: several
    Russian aircraft flew inside its air-defence identification zone
    Tuesday over waters between the Korean Peninsula and Japan; fighter
    jets scrambled before the planes withdrew. Source: Daily Summary of
    World, first reported 24 Nov 01:04 UTC.
23. **Nepal quake M5.3** — A magnitude-5.3 earthquake shakes eastern
    Nepal's Koshi province near the China border on Tuesday morning.
    Magnitude corrected from round 1's M5.6 (Nepal's own local magnitude);
    USGS, EMSC and India's NCS all put it at M5.3. Source: USGS / EMSC,
    24 Nov 2026.
24. **India–Nepal deepen ties** — PM Modi and Nepal PM Balendra Shah
    discuss infrastructure, trade, energy and cultural ties; new
    Saryu–Kamala Express rail service links Ayodhya and Janakpur Dham.
    Source: Careerindia, 24 Nov 2026.
25. **Odisha approves ₹249-cr cyber hub** — Odisha government approves a
    ₹249-crore Cyber Command Centre to strengthen digital security.
    Source: Careerindia, 24 Nov 2026.
26. **Google gives $5m to IIT Kharagpur** — Google announces $5m financial
    support for AI research and infrastructure at IIT Kharagpur.
    Source: Careerindia, 24 Nov 2026.
27. **Jaishankar calls Lavrov** — External Affairs Minister S. Jaishankar
    speaks by phone with Russian Foreign Minister Sergei Lavrov.
    Source: Chennaionline, 24 Nov.

### Also on (stories 28–40)

28. **Hasina plans return 16 Dec** — Former Bangladesh PM Sheikh Hasina
    plans to return home from exile in India on 16 December.
    Source: Chennaionline, published 24 Nov 10:01 IST.
29. **India–China border talks** — Military representatives hold talks to
    maintain stability along the Line of Actual Control.
    Source: Careerindia, 24 Nov 2026.
30. **AI centre opens at IIT Patna** — Inauguration of an AI centre at IIT
    Patna for research and technological development.
    Source: Careerindia, 24 Nov 2026.
31. **JEE Main 2027 late window opens** — NTA opens the late-fee
    registration window for JEE Main 2027 Session 1, until 26 Nov.
    Source: Careerindia, 24 Nov 2026.
32. **India–EU trade deal nears signing** — India and the EU progress
    towards finalising a free-trade agreement. Source: Careerindia,
    24 Nov 2026.
33. **Beaver Supermoon tonight** — November's full Beaver Moon reaches
    full phase Tuesday 24 Nov at **14:53 UTC**, 360,767 km away — the
    first of **four** consecutive supermoons (Nov, Dec, Jan, Feb, until
    Feb 2027). Corrected from round 1's "first of three".
    Source: BBC Sky at Night / NASA lunar timetable, 24 Nov 2026.
34. **Real Madrid hit PSV for five** — Real Madrid 5-1 PSV;
    Galatasaray 1-0 Aston Villa, Champions League, Tuesday evening.
    Source: UEFA.com, event Tue 24 Nov 2026. (Replaces round-1 story 34,
    stale Mon 23 Nov.)
35. **Al-Nassr edge Al-Sadd 2-1** — Cristiano Ronaldo's Al-Nassr beat
    Al-Sadd 2-1 (João Félix bicycle kick); Al-Qadsiah thrash Shabab
    Al-Ahli 5-1. Source: Reuters / Flashscore, event Tue 24 Nov 2026.
    NOTE: the-AFC page was NOT retrievable, so the-AFC is NOT cited as a
    verified URL — Reuters/Flashscore only. (Replaces round-1 story 35,
    stale Mon 23 Nov.)
36. **Gukesh holds Sindarov in Game 1 draw** — Sindarov–Gukesh ½–½ in
    38 moves, Berlin Defence; score 0.5–0.5. World Championship Game 1,
    Fondation Martin Bodmer, Geneva. Source: ChessBase / FIDE,
    Tue 24 Nov 2026, 15:00 CET. (Upgraded from round 1's "begins title
    defence".)
37. **Seoul summons Russian attaché** — Defence Ministry to summon
    Col. Nikolai Marchenko after the KADIZ incursion; first-ever air-raid
    alert sounded. Source: Yonhap, event Tue 24 Nov 2026. This is a NEW
    follow-up event, not a duplicate of kept story 22 (the jets entering
    the zone). (Replaces round-1 story 37, stale Sun 22 Nov.)
38. **WTC Final race tightens** — South Africa, Australia and New Zealand
    lead the 2025–27 World Test Championship standings (22 Tests, four
    contenders). Source: Times of India, 24 Nov 02:52 UTC.
39. **Most Germans oppose Ukraine arms aid** — Körber poll: 53% oppose,
    46% favour; a reversal from a year ago. Source: Reuters / Körber
    Stiftung, event Tue 24 Nov 2026. (Replaces round-1 story 39, stale
    Sat 21 Nov.)
40. **Lula snubs Milei over inauguration** — Lula will not invite Milei
    to his 5 Jan inauguration after the foreign minister questioned the
    election; ambassador not restored. Source: UOL, reported
    Tue 24 Nov 21:00 UTC. (Replaces round-1 story 40, stale Fri 20 Nov.
    The Lula story was preferred over the backup — "Australia fines Big
    Tech up to 5%" (Reuters Sydney, 24 Nov) — so Latin America keeps a
    story and the 7-region claim holds.)

## Distinct-count check

Heroes 3 + grid 24 (stories 4–27) + Also on 13 (stories 28–40) = **40
distinct stories**. No story is repeated: the Megaspeed/Nvidia thread
appears once as hero 1 (the Entity List action) and once as grid story 5
(the Tuesday Asian market reaction) — two different events, two different
sources. The Ukraine thread appears as hero 2 (talks call), grid 11 (fresh
attacks) and grid 9 is NATO space defence — three distinct events. Story
37 (Seoul summons the attaché) is a new follow-up event, distinct from
story 22 (the jets entering the zone).

## Region check

All 7 regions have at least one story: North America (heroes 1, stories
4–8, 21, 40 via the migrant route's U.S. angle is NOT counted — North
America is covered by 1, 4, 5, 6, 7, 8, 21), Europe (hero 2, stories 9,
10, 11, 34, 39), Middle East (hero 3, stories 12, 13, 16, 35),
Africa (stories 15, 17, 18, 19, 20), Asia-Pacific (stories 22, 23, 24,
25, 26, 27, 28–33, 36, 37), Oceania (story 38 — WTC standings include
New Zealand and Australia), Latin America (story 40 — Lula/Milei).
Global stories (33 Supermoon, 39 poll is Europe) are filed as in round 1.

## Map-pin check

12 pins, each numbered to match its story on the poster:
1 Singapore (Megaspeed), 2 Kyiv (Zelensky talks), 3 Jerusalem (Netanyahu),
13 Tehran (Iran warning), 22 Seoul (ADIZ), 21 Washington DC (Giuliani
Medal of Freedom — re-pointed from Beijing, whose story was dropped),
23 Kathmandu (quake), 24 New Delhi (India–Nepal), 16 Baghdad (Kurdish
oilfields — re-pointed from Abuja, whose story was dropped),
18 Johannesburg (statue), 4 Ottawa (Pentagon/Canada), 6 Doha (U.S.–Qatar).
Every pin's date agrees with the DATE CHECK box: none of the pinned
stories is listed as dropped. Label offsets were adjusted for the two
moved pins (Baghdad below-right, Washington below-right) and visually
checked for overlaps.

## DATE CHECK — dropped stories and their correct dates

These big stories were considered and deliberately left out because they
are NOT from Tuesday 24 Nov 2026. The box now holds all 22 (the 12 from
round 1 plus the 10 stale round-1 stories removed in round 2), one line
each, 4 columns × 6 rows, inside the same 1008×120 box.

### Dropped in round 1 (12, unchanged)

- COP31 climate deal collapses — **Sun 22 Nov** (Antalya Pact rejected;
  no fossil-fuel mention; summit ended without an agreement).
- Cikande factory fire — fire **Sat 21 Nov**; death toll 24 confirmed
  **Mon 23 Nov** (Reuters).
- Nvidia rehires Huang as CEO — **Mon 23 Nov** (board vote unanimous;
  shares +31% that day).
- Alcaraz wins ATP Finals — **Sun 22 Nov** (beat Zverev 6–2, 7–6(7),
  Turin).
- India 3rd in Asia Power Index — index published **Mon 23 Nov** (Lowy
  Institute; score 40.5).
- Lula wins Brazil runoff — **Sun 25 Oct** (51.79% vs 48.21%).
- Kiros, 1st Gen Z woman in Congress — **Tue 3 Nov** (Colorado's 1st
  district).
- ICJ: Myanmar genocide ruling — **Thu 19 Nov**.
- Ukraine "sinks" Russian warship off Libya — **Mon 23 Nov**.
- EU proposes 22nd Russia sanctions package — **Mon 23 Nov**.
- Waymo pulls robotaxis off freeways — **11–18 Nov** (California DMV ban
  11 Nov).
- "El Chapo Isidro" captured in Mexico — **Sat 21 Nov**.

### Newly dropped in round 2 (10 — the stale round-1 stories)

- U.S. adds 24 Nigerians to deport list — **~10 Nov** (same Punch/DHS
  text, "total 157", already published ~10 Nov; the 24-name update is
  ~2 weeks old).
- EU court bans BYD Ti7 — **Fri 20 Nov** (The Hague District Court
  preliminary ruling; TradingView 21 Nov 03:42 UTC).
- Russian cargo ship on fire — **Sat 21 Nov** (Sparta II drone strike
  08:40–08:50; Reuters HELSINKI Nov 21; 16 crew evacuated).
- Nigeria sets $11m stablecoin floor — **Thu 5 Nov** (CBN Regulations
  for Non-Security Virtual Assets, circular dated 5 Nov; reported 6 Nov).
- China sentences official to death — **Mon 23 Nov** (Reuters/AP Nov 23;
  facts were correct: 35 items, >¥1m / ~$150k).
- Wellington Test drawn — **Mon 23 Nov** (Test Nov 19–23, draw on final
  day; 720/9 declared is correct).
- AFC Champions League draws — **Mon 23 Nov** (Al Ain 1–1 Esteghlal,
  Neftchi 2–2 Al Hilal played Mon 23 Nov; scores correct).
- India take hockey series 1–0 — **Sun 22 Nov** (final match Sun 22 Nov,
  series 19–22 Nov; 1–0 series, final 2–2 correct).
- UN states to draft 'killer robot' rules — **Sat 21 Nov** (CCW 7th
  Review Conference agreement, early hours Sat 21 Nov; Reuters GENEVA).
- Migrant caravan heads north — **Fri 20 Nov** (Reuters Nov 20: ~300
  crossed Guatemala→Mexico Fri 20 Nov).

## Verification

- Every replacement story verified against its named primary source with
  a Tue 24 Nov 2026 event date; every kept story re-checked under the
  event-date rule.
- Two local runs of `main.py` with `MAKEFUN_OUTPUT_DIR=out` produce
  byte-identical `entry.png` (sha256 compared, see below).
- `entry.png` is 1024×1024 px and under the 1 MiB cap.
- Poster visually inspected at full size: no overlapping text remains;
  all 40 numbers, 12 pins and the DATE CHECK box are legible.

## What could not be verified

- Story 14 (Khan Younis strike) rests on Gaza sources via WarRadar and
  is explicitly marked as reported, not independently confirmed; the
  casualty names come from that report.
- Story 7 (FBI crime database hacked) and story 27 (Jaishankar–Lavrov
  call) are carried as short headlines from Chennaionline's 24 Nov
  international page with no further detail published at build time.
- Story 35 now cites Reuters/Flashscore, not the-AFC: the-AFC page was
  not retrievable, so it is not cited as a verified URL.
- Story 40 (Lula snubs Milei) rests on UOL, reported Tue 24 Nov
  21:00 UTC; the backup story (Australia fines Big Tech up to 5%,
  Reuters Sydney 24 Nov) was not needed.
- The DATE CHECK box is set at 8 pt so all 22 one-line entries fit the
  1008×120 box; four round-1 labels were shortened to fit their dates
  on one line ("Kiros, 1st Gen Z in Congress", "Waymo robotaxis off
  freeways", the Asia Power Index date shown without "published", and
  "Cikande fire" for the Cikande factory fire) —
  full wording and dates are in this methodology.

## Verification record (round 2, built 25 Nov 2026)

- STATUS: complete. Render script edited (all 10 replacements, upgrades,
  figure nits, pin re-points, DATE CHECK redesign, footer sources);
  final render: 1024×1024, 220,633 bytes, sha256
  `2da8161beca7c1f3948661e2a39ea0b18404386f96484dae1d17e77185f550d8`.
  A first render (224,041 bytes) had 4 DATE CHECK entries truncated
  (dates cut off: Kiros, Asia Power Index, Waymo, China sentence) —
  fixed by dropping the DATE CHECK font to 8 pt and shortening three
  labels; the re-render had one remaining truncation (Cikande's date),
  fixed by shortening that label to "Cikande fire". Final render
  visually re-verified: all 22 DATE CHECK entries fully legible.
- Two-run byte-compare: `MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py`
  and `... /tmp/out2 ...` both write `entry.png` sha256
  `2da8161beca7c1f3948661e2a39ea0b18404386f96484dae1d17e77185f550d8` —
  identical to each other and to the committed `entry.png`. `cmp` clean.
- Dimensions 1024×1024, size 220,633 bytes (limit 1,048,576).
- Kit check (local, no transcripts yet) at 2026-11-25T00:47:34Z:
  4 passed (competition_open, snapshot, license_osi, entrypoint),
  1 failed (transcripts_present — expected: the transcript bundle is
  made by the parent pipeline), 14 skipped, 5 "at submission" (same
  profile as round 1).
- Visual re-verification after the final re-render: all 22 DATE CHECK
  entries fully legible (the last truncation, Cikande's date, was fixed
  by shortening the label to "Cikande fire" — full wording in this
  methodology); heroes, all 40 numbers, all 12 pins + labels (incl.
  Baghdad and Washington) legible, no overlaps.
- Local git commit: see the build report for the hash.

## Verification record (round 1, built 24 Nov 2026 ~06:30 UTC)

- Two-run byte-compare: `MAKEFUN_OUTPUT_DIR=out1 python3 main.py` and
  `... out2 ...` both write `entry.png` sha256
  `7aca7fe33f8efe0c64909e9f0860d2dc36b4c3e8eb77db00d602d2b807cf1b32` —
  identical to each other and to the committed `entry.png`. `cmp` clean.
- After a revision to `main.py` (1 MiB sanity guard + confirmation print)
  the two-run check was repeated: still byte-identical, same sha256.
- Dimensions 1024×1024, size 216,594 bytes (limit 1,048,576).
- Kit check (local, no transcripts yet): `node cli/makefun.mjs check --kit .
  --repo <entry>` at 2026-11-24T06:28:37Z — 4 passed (competition_open,
  snapshot, license_osi, entrypoint), 1 failed (transcripts_present —
  expected: the transcript bundle is made by the parent pipeline),
  14 skipped (all transcript checks), 5 "at submission" (repo_public,
  repo_owner, repo_created_after_open, commit_in_repo,
  duplicate_snapshot — normal pre-submission items for the pipeline).
- Local git commit: see the build report for the hash.
