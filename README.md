[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/17T-ProGimank/makefun-news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/17T-ProGimank/makefun-news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

# The World in One Day — Tuesday 24 November 2026

**40 sourced stories, 7 regions — U.S. blacklists Megaspeed, Zelensky calls
for four-way talks, Netanyahu presses Trump on Iran; all figures checked
against live sources on Tuesday 24 November 2026.**

Round 1 of the 24 November front page. All three leads are genuine
Tuesday 24 November 2026 events, first reported that day in UTC: the U.S.
Bureau of Industry and Security puts Singapore-based Megaspeed and six
other firms on the Entity List (00:52 UTC); President Zelensky calls by
video for a four-party meeting with Russia, the U.S. and Europe (00:30
UTC); and Prime Minister Netanyahu urges President Trump to launch fresh
strikes on Iran (Kan report, Tuesday morning). Plus 24 numbered stories, 13
more in "Also on", a 12-pin world map, and a DATE CHECK box listing the big
stories deliberately left out because they are not from Tuesday.

What the audit caught before the build: the Cikande factory fire broke out
Saturday 21 Nov (toll 24 confirmed Monday 23 Nov), COP31 collapsed Sunday
22 Nov, Nvidia rehired Jensen Huang on Monday 23 Nov, Alcaraz won the ATP
Finals on Sunday 22 Nov, the Asia Power Index was published Monday 23 Nov,
and the Lula runoff, the Kiros election and the ICJ Myanmar ruling are all
older — every one of them is named in the DATE CHECK box with its correct
date instead of being shown as Tuesday's news.

- **Bounty:** [news-image-20261124 on make.fun](https://make.fun/bounty/news-image-20261124)
- **Entry:** `main.py` (Python 3.13, stdlib only) copies the pre-rendered
  `entry.png` (1024×1024, 40 stories) to `$MAKEFUN_OUTPUT_DIR/entry.png`.
  The poster was drawn offline with Pillow + DejaVu (render script kept in
  the builder's work dir) because the grader's pinned Python image ships no
  Pillow and no system fonts — the entrypoint itself imports nothing beyond
  the standard library.
- **Verification:** every story is attributed to its source with a
  first-reported time where one was published; the DATE CHECK box names the
  stories left out on purpose. Two local runs are byte-identical.

Built with [make.fun](https://make.fun/r/m4psg5rh) — my referral link.
