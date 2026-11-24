# Methodology — news-image-20261124 (round 1)

## What this entry is

A one-page newspaper poster summing up the world news of **Tuesday
24 November 2026**: masthead + 3 hero stories + 24 numbered grid stories +
13 "Also on" stories + a 12-pin world map + a DATE CHECK box + a sources
footer. **40 distinct stories across 7 regions** (North America, Europe,
Middle East, Africa, Asia-Pacific, Oceania, Latin America; the Beaver
Supermoon and the UN "killer robots" agreement are filed under Global).

## Model

- `main.py` is Python 3.13, standard library only. It copies the
  pre-rendered `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`. The grader's
  pinned Python image is bare stdlib (no Pillow, no fonts), so the poster
  is rendered locally beforehand with Pillow + DejaVu and committed at the
  repo root. The render script lives in the builder's work directory, not
  in the entry.
- `entry.png`: 1024×1024 px, 216,594 bytes (limit 1 MiB),
  sha256 `7aca7fe33f8efe0c64909e9f0860d2dc36b4c3e8eb77db00d602d2b807cf1b32`.
- Two local runs (`MAKEFUN_OUTPUT_DIR=out`, run twice) produce
  byte-identical output — verified, see "Verification" below.

## Date rule

A story counts only if it **happened, or was first reported, on Tuesday
24 November 2026 in some time zone**. Every story below carries the source
and the first-reported time or publication date found in live checks on
24 Nov 2026 (~06:00–06:30 UTC). Stories that failed the date test were
dropped and are listed in the DATE CHECK section with their correct dates.

## The 40 stories (verified)

### Heroes

1. **U.S. blacklists Megaspeed in Nvidia spy case** — U.S. Bureau of
   Industry and Security places Singapore-based Megaspeed International
   and six other Southeast Asian firms on the Entity List; licences now
   required for advanced U.S. technology, including Nvidia GPUs.
   Source: Daily Summary of World, first reported 24 Nov 00:52 UTC.
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
5. **Asian markets rally on Huang return** — Asian stocks gain Tuesday
   after Nvidia's +31% Monday rebound on Jensen Huang's reinstatement
   (Nasdaq +6.5%, S&P 500 +4.7% Monday). Source: Chennaionline, 24 Nov.
6. **U.S. & Qatar deepen ties** — U.S. and Qatar agree to strengthen
   cooperation in defence, trade and technology. Source: Chennaionline,
   24 Nov.
7. **FBI crime database hacked** — FBI's crime database hit in a new cyber
   attack. Source: Chennaionline, 24 Nov.
8. **U.S. adds 24 Nigerians to deport list** — Total on the deportation
   list rises to 157. Source: The Africa Media, 24 Nov 2026.
9. **NATO vows space defence** — NATO chief Mark Rutte: alliance will
   defend against threats in space after reports Russia could launch a
   nuclear-armed satellite ("Sputnik-S") as early as December 2026.
   Source: Ungated Brussels timeline, 24 Nov 2026.
10. **EU court bans BYD Ti7** — The Hague court provisionally bans the BYD
    Ti7 in the EU for resembling the Defender too closely; bars imports,
    production and storage. BYD disputes the ruling, plans to appeal.
    Source: Paris Times, Business, 24 Nov 2026.
11. **Fresh Russian attacks on Kyiv** — Ukrainian authorities report new
    drone and missile strikes in the Kyiv region. Source: Careerindia,
    24 Nov 2026.
12. **Russian cargo ship on fire** — Russian cargo vessel catches fire in
    the Gulf of Finland following a drone-related incident; all 16 crew
    evacuated safely. Source: Careerindia, 24 Nov 2026.
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
16. **Nigeria sets $11m stablecoin floor** — Central Bank of Nigeria
    confirms a ₦15bn ($11m) capital floor for foreign-currency stablecoin
    issuers, local incorporation and 100% reserves + 2% buffer.
    Source: BetaBriefing, 24 Nov 2026.
17. **Nigeria trade surplus falls 31%** — Monthly trade surplus down
    31.44% month-on-month to $2.03bn in July from $2.96bn in June.
    Source: Vanguard Nigeria, 24 Nov 03:28 UTC.
18. **Africa's first 'comfort women' statue** — A statue of a girl
    symbolising the victims of Japan's wartime "comfort women" system to
    be unveiled in South Africa. Source: Yonhap News, 24 Nov 01:18 UTC.
19. **CAS to rule on AFCON title today** — Court of Arbitration for Sport
    to deliver its verdict Tuesday on Senegal's appeal against the
    withdrawal of its 2025 AFCON championship. Source: Matrix News,
    24 Nov 2026.
20. **S. Africa: rape arrests top 50 a day** — Rape arrests top 50 a day
    as the 16 Days of Activism campaign approaches. Source: IOL,
    24 Nov 03:30 UTC.
21. **China sentences official to death** — Chinese official surnamed Ma
    sentenced to death for spying for an unnamed foreign country; recruited
    while working abroad, provided 35 classified items, received over
    1 million yuan (~$150,000). Source: Daily Summary of World (Gold Wall
    Press), first reported 24 Nov 02:37 UTC.
22. **Russian jets enter S. Korea zone** — South Korea's military: several
    Russian aircraft flew inside its air-defence identification zone
    Tuesday over waters between the Korean Peninsula and Japan; fighter
    jets scrambled before the planes withdrew. Source: Daily Summary of
    World, first reported 24 Nov 01:04 UTC.
23. **Nepal quake M5.6** — A 5.6-magnitude earthquake shakes eastern
    Nepal's Koshi province near the China border on Tuesday morning.
    Source: Chennaionline, 24 Nov.
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
    full phase Tuesday 24 Nov at 14:54 UTC, 360,767 km away — the first
    of three consecutive supermoons. Source: NASA lunar timetable /
    AstroSlide, 24 Nov 2026.
34. **Wellington Test drawn** — First Test, India vs New Zealand at
    Wellington, ends in a draw; India declared 720/9, New Zealand hold on
    on the final day. Source: Careerindia, 24 Nov 2026.
35. **AFC Champions League draws** — Al Ain (UAE) 1–1 Esteghlal (IRN);
    Neftchi (UZB) 2–2 Al Hilal (KSA), Tuesday 24 Nov. Source: the-AFC,
    24 Nov 2026.
36. **Gukesh begins title defence** — India's D Gukesh starts his World
    Championship title defence against Uzbekistan's Javokhir Sindarov in
    Geneva. Source: Careerindia, 24 Nov 2026.
37. **India take hockey series 1–0** — Indian men's hockey team secure a
    1–0 series win over New Zealand; final match ends 2–2.
    Source: Careerindia, 24 Nov 2026.
38. **WTC Final race tightens** — South Africa, Australia and New Zealand
    lead the 2025–27 World Test Championship standings (22 Tests, four
    contenders). Source: Times of India, 24 Nov 02:52 UTC.
39. **UN states to draft 'killer robot' rules** — Nations agree to
    elaborate rules for AI-run weapons ("killer robots") by 2028.
    Source: Al Jazeera, 24 Nov 2026.
40. **Migrant caravan heads north** — Around 300 migrants cross from
    Guatemala into Mexico, walking towards the U.S. border.
    Source: Al Jazeera, 24 Nov 2026.

## Distinct-count check

Heroes 3 + grid 24 (stories 4–27) + Also on 13 (stories 28–40) = **40
distinct stories**. No story is repeated: the Megaspeed/Nvidia thread
appears once as hero 1 (the Entity List action) and once as grid story 5
(the Tuesday Asian market reaction) — two different events, two different
sources. The Ukraine thread appears as hero 2 (talks call), grid 11 (fresh
attacks) and grid 9 is NATO space defence — three distinct events.

## Map-pin check

12 pins, each numbered to match its story on the poster:
1 Singapore (Megaspeed), 2 Kyiv (Zelensky talks), 3 Jerusalem (Netanyahu),
13 Tehran (Iran warning), 22 Seoul (ADIZ), 21 Beijing (spy sentence),
23 Kathmandu (quake), 24 New Delhi (India–Nepal), 16 Abuja (CBN rules),
18 Johannesburg (statue), 4 Ottawa (Pentagon/Canada), 6 Doha (U.S.–Qatar).
Every pin's date agrees with the DATE CHECK box: none of the pinned
stories is listed as dropped.

## DATE CHECK — dropped stories and their correct dates

These big stories were considered and deliberately left out because they
are NOT from Tuesday 24 Nov 2026:

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

## Verification

- Every hero verified against its named source in live checks on
  24 Nov 2026; every grid/also-on story carries a source dated 24 Nov.
- Two local runs of `main.py` with `MAKEFUN_OUTPUT_DIR=out` produce
  byte-identical `entry.png` (sha256 compared, see below).
- `entry.png` is 1024×1024 px and 216,594 bytes, under the 1 MiB cap.
- Poster visually inspected at full size and in crops (heroes, map):
  no overlapping text remains; all 40 numbers, 12 pins and the DATE CHECK
  box are legible.

## What could not be verified

- Story 14 (Khan Younis strike) rests on Gaza sources via WarRadar and
  is explicitly marked as reported, not independently confirmed; the
  casualty names come from that report.
- Story 7 (FBI crime database hacked) and story 27 (Jaishankar–Lavrov
  call) are carried as short headlines from Chennaionline's 24 Nov
  international page with no further detail published at build time.
- The Champions League matchday-5 evening fixtures (e.g. Galatasaray vs
  Aston Villa) had not kicked off at build time (~06:30 UTC), so no
  result is claimed; the AFC Champions League results (story 35) are the
  day's completed football.
- The CAS verdict on the AFCON title (story 19) was due later on Tuesday;
  the poster says "to rule today" and claims no outcome.

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
