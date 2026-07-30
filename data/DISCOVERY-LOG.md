
## 2026-07-22 — Apify competitor seed

- 22 clips >=1M plays seeded from competitor scrape


| Owner | Plays | Dur | Date | Speaker | URL |
|---|---|---|---|---|---|
| theaipage | 23121461 | 29s | 2024-07-15 | - | https://www.instagram.com/p/C9dFOcRN9m3/ |
| thewizeai | 6266415 | 32s | 2026-03-24 | - | https://www.instagram.com/p/DWRnMAhgXev/ |
| airesearches | 5281945 | 23s | 2026-06-19 | - | https://www.instagram.com/p/DZwxxKkssQM/ |
| evolving.ai | 3899335 | 100s | 2026-07-11 | - | https://www.instagram.com/p/DaqAxNDzbfk/ |
| airesearches | 3260522 | 77s | 2026-07-03 | - | https://www.instagram.com/p/DaUZ6SWKkrK/ |
| airesearches | 2913089 | 45s | 2026-06-17 | - | https://www.instagram.com/p/DZr-edMsdKw/ |
| evolving.ai | 2671474 | 274s | 2026-06-18 | - | https://www.instagram.com/p/DZuh9jkg7QR/ |
| airesearches | 2109208 | 107s | 2026-07-17 | - | https://www.instagram.com/p/Da4YBQjqWHy/ |
| airesearches | 2085238 | 83s | 2026-07-05 | - | https://www.instagram.com/p/DaaKVPfqlLe/ |
| evolving.ai | 1611671 | 82s | 2026-07-04 | - | https://www.instagram.com/p/DaXGN3YzaVH/ |
| evolving.ai | 1579273 | 64s | 2026-07-13 | - | https://www.instagram.com/p/DavETSJTfpM/ |
| evolving.ai | 1502022 | 147s | 2026-07-01 | - | https://www.instagram.com/p/DaQdXyaTqek/ |
| evolving.ai | 1459427 | 88s | 2026-06-18 | - | https://www.instagram.com/p/DZt0MDhz42M/ |
| airesearches | 1418249 | 13s | 2026-06-18 | - | https://www.instagram.com/p/DZtpnONMzk4/ |
| evolving.ai | 1384596 | 64s | 2026-07-07 | - | https://www.instagram.com/p/DafiXAhToEX/ |
| evolving.ai | 1373406 | 119s | 2026-06-25 | - | https://www.instagram.com/p/DZ_6sY0Tow6/ |
| evolving.ai | 1281917 | 15s | 2026-07-03 | - | https://www.instagram.com/p/DaU-l4lTj2w/ |
| evolving.ai | 1208107 | 36s | 2026-07-08 | - | https://www.instagram.com/p/DaivyqBzcYS/ |
| evolving.ai | 1131362 | 28s | 2026-07-01 | - | https://www.instagram.com/p/DaP3SX_zXO4/ |
| airesearches | 1069428 | 36s | 2026-07-18 | - | https://www.instagram.com/p/Da7kkKlKMJG/ |
| airesearches | 1054183 | 64s | 2026-07-04 | - | https://www.instagram.com/p/DaXOfU-qG6s/ |
| evolving.ai | 1001992 | 156s | 2026-06-22 | - | https://www.instagram.com/p/DZ5DZotNS3c/ |

## 2026-07-22 — Daily discovery run (X/Twitter + speaker search)

**@theaibolt refresh:** Apify `apify/instagram-reel-scraper` sweep (200-result limit, 142 items returned of 143 known posts) found **zero new posts** since the last sweep — posted_urls list unchanged. No pruning needed this run. Speaker saturation on theaibolt: Jensen Huang 15, Sam Altman 14, Dario Amodei 11, Elon Musk 12, Geoffrey Hinton 5, Zuckerberg 9, Mo Gawdat 3, Bengio 1.

**Seed audit:** the 22 clips seeded earlier today (competitor theme-page sweep of @airesearches/@evolving.ai/@thewizeai/@theaipage, table above) were reviewed against the FORMAT criterion and **rejected wholesale** — every one is AI-generated/CGI video (sports recreations, robot fights, meme edits) with no real speaker (`speaker` field empty on all 22). None were promoted to the backlog. This confirms the routine's own warning that most 1M+ AI content on IG theme pages is AI-generated video, not real-person interviews.

**Discovery (available < 100, topped up):** ran the two untried levers flagged in the 2026-07-09 status note — (a) X/Twitter search via `api-ninja/x-twitter-advanced-search`, untried until now; (b) direct speaker-name + cross-industry keyword search on Instagram via `data-slayer/instagram-search-reels`, covering Tier 2/3 AI researchers and non-tech fields (medicine, law, finance, music, sports, publishing, film, politics). Three parallel searches, ~40 queries total.

**Result:** +9 clean additions to `available`, +5 flagged to `review` (too-short duration or unconfirmed source/authenticity), +1 view-count refresh (Jeremy Grantham 6.8M → 7.58M — the cross-industry search re-surfaced this existing backlog clip rather than a new one).

Backlog now **19/100 available** (was 10), **6 review** (was 1). Still well short of the 90-alert threshold — IG keyword search on individual speaker names mostly surfaces sub-1M aggregator reposts (e.g. Andrej Karpathy searches topped out at 366K views across 24 results), confirming the account-list exhaustion already noted 2026-07-09 extends to speaker-name search too. X/Twitter search is the most promising underused lever going forward and deserves deeper investment (more query variants, media-type/engagement tuning) in future runs. The Priority-1 lever (mining the original full-length source interview behind each of theaibolt's 143 posts to find proven 1M+ candidates) was **not attempted** this run — the scope (143 individual source-research lookups) is too large for a single session; flagging as a dedicated future-run project.

### New additions (available)

| Speaker | Views | Field | Source | Pillar | URL |
|---|---|---|---|---|---|
| Palmer Luckey | 11,307,914 | Tech/Defense | The Free Press / Honestly | Controversial | https://www.instagram.com/reel/DQUhcagkvOj/ |
| Jensen Huang | 5,387,199 | Tech (Nvidia) | GTC keynote | Educational | https://twitter.com/mreflow/status/1663244486091194368 |
| Ben Affleck | 4,444,313 | Film | Unconfirmed | Educational | https://twitter.com/Hesamation/status/2078565094779244802 |
| Geoffrey Hinton | 4,206,116 | AI research | 60 Minutes (CBS) | Controversial | https://www.instagram.com/reel/DN1KONh3q8z/ |
| Tristan Harris | 3,723,343 | AI safety/ethics | Milken Institute | Controversial | https://www.instagram.com/reel/DY48YG9ILQ-/ |
| Daniel Kokotajlo | 2,776,356 | AI safety (ex-OpenAI) | Diary of a CEO | Controversial | https://www.instagram.com/reel/DauWOAdBU6w/ |
| Mo Gawdat | 1,826,310 | Tech (ex-Google X) | Diary of a CEO | Controversial | https://www.instagram.com/reel/DM8ctKUu46P/ |
| Mo Gawdat | 1,447,836 | Tech (ex-Google X) | Diary of a CEO | Emotional | https://www.instagram.com/reel/Cs8ERfuAQn4/ |
| Palmer Luckey | 1,442,305 | Tech/Defense | Joe Rogan Experience #2394 | Controversial | https://www.instagram.com/reel/DYmksjDoykn/ |

Pillar mix this batch skewed heavily Controversial (7 of 9) since safety/warning stories were the highest-yield content this run — future sourcing should target more Educational/Inspirational picks to rebalance toward the target mix (Educational majority, ~25% Controversial, ~10% Emotional, remainder Inspirational).

### Flagged to review (not promoted — need manual confirmation)

| Speaker | Views | Reason | URL |
|---|---|---|---|
| Geoffrey Hinton (via @elonmusk repost) | 37,789,246 | Source/duration unconfirmed; 5th Hinton clip risks over-saturation | https://twitter.com/elonmusk/status/1801976488251814048 |
| Boris Johnson | 3,586,917 | Only 7.5s; caption reads auto-generated; cannot confirm authentic unedited footage | https://www.instagram.com/reel/DWyvY17iDEz/ |
| Cassie Alexander (@theladysparks) | 2,457,930 | Only 5.4s; speaker not well-known; format borderline (reaction clip, not interview) | https://www.instagram.com/reel/DSarp4aD6ft/ |
| Elon Musk | 2,428,297 | Quote-card style repost; could not confirm on-camera video vs b-roll; Elon saturated | https://twitter.com/MarioNawfal/status/1885645176774816217 |
| Elon Musk | 1,478,311 | Only 9.2s; too short to confirm genuine interview/Q&A format | https://www.instagram.com/reel/DC1yyERPTX3/ |

### Hooks for top 3 new additions

**Palmer Luckey — ChatGPT jailbreak story (11.3M views)**
1. Palmer Luckey tricked ChatGPT with a story it could not resist.
2. Palmer Luckey found ChatGPT's one weakness. It was not a hack.
3. Palmer Luckey played pretend with ChatGPT. It broke its own rules.

**Jensen Huang — GTC NPC dialogue demo (5.4M views)**
1. Jensen Huang showed a game character that thinks on its own.
2. Jensen Huang put real thought inside a video game. Nobody wrote it.
3. Jensen Huang changed video games forever with three words on stage.

**Ben Affleck — AI in Hollywood (4.4M views)**
1. Ben Affleck says AI will not replace filmmakers. Here is why.
2. Ben Affleck explained how AI is already remaking Hollywood in secret.
3. Ben Affleck revealed the one job AI still cannot steal.

### Apify quota status
No quota, auth, or billing errors encountered across any of the actor runs this session (`apify/instagram-reel-scraper`, `data-slayer/instagram-search-reels`, `api-ninja/x-twitter-advanced-search`). All runs SUCCEEDED.

## 2026-07-23 — X/Twitter search top-up (+9 net-new, union-deduped by shortcode)

**Backlog status at run start:** 25/100 available (post 2026-07-22 batch), well short of the 90-alert threshold.

**Discovery:** continued X/Twitter search via `api-ninja/x-twitter-advanced-search`, focused on Anthropic/DeepMind-adjacent speakers not yet in the backlog (Dario Amodei, Demis Hassabis, Andrej Karpathy) plus a non-CEO finance voice (Krishna Rao) and a contrarian media voice (Ed Zitron).

**Result:** +9 clean additions, all promoted directly to `available` (no review-tier flags this batch). Backlog now **34/100 available** (was 25). Still well short of 90 — no BACKLOG NEAR CAP alert warranted.

### New additions (available)

| Speaker | Views | Field | Source | Pillar | URL |
|---|---|---|---|---|---|
| Dario Amodei | 3,487,899 | AI (Anthropic CEO) | Congressional/lawmaker testimony (UNCONFIRMED exact hearing) | Controversial | https://x.com/coinbureau/status/2071330294452666695 |
| Krishna Rao | 3,225,977 | Finance (Anthropic CFO) | Patrick O'Shaughnessy's podcast (confirmed) | Educational | https://x.com/patrick_oshag/status/2054532117410054252 |
| Andrej Karpathy | 3,189,981 | AI research (ex-Tesla/OpenAI, now Anthropic) | UNCONFIRMED - interview name not given | Educational | https://x.com/rewind02/status/2056850947947827403 |
| Ed Zitron | 1,980,561 | Tech media / AI critic | CNBC (confirmed from caption) | Controversial | https://x.com/edzitron/status/2072703921768837195 |
| Dario Amodei | 2,409,121 | AI (Anthropic CEO) | UNCONFIRMED - 3-hour podcast, name not given | Educational | https://x.com/shmidtqq/status/2067724728110854456 |
| Dario Amodei | 1,380,680 | AI (Anthropic CEO) | The Economist (confirmed via web search) | Emotional | https://x.com/r0ck3t23/status/2027698383037591957 |
| Dario Amodei | 1,368,545 | AI (Anthropic CEO) | Bloomberg interview (confirmed from caption) | Emotional | https://x.com/dubeyamitabh/status/2067619253600321574 |
| Dario Amodei | 1,251,951 | AI (Anthropic CEO) | Widely-quoted Amodei statement - exact original interview UNCONFIRMED | Controversial | https://x.com/JesseCohenInv/status/2019051610207383745 |
| Demis Hassabis | 1,284,747 | AI research (Google DeepMind CEO, Nobel laureate) | UNCONFIRMED - interview name not given | Educational | https://x.com/Ric_RTP/status/2065430321550467149 |

Dario Amodei now has 5 clips in this single batch alone — heavy saturation, space postings out aggressively when scheduling; do not source further Dario clips until several of these are posted.

### Hooks for top 3 new additions

**Dario Amodei — open source AI 'very dangerous path' warning to lawmakers (3.5M views)**
1. Dario Amodei warned lawmakers about a danger nobody can undo.
2. Dario Amodei said one AI decision cannot be taken back. Ever.
3. Dario Amodei told Congress the real risk isn't the AI itself.

**Krishna Rao — Anthropic's revenue growth story (3.2M views)**
1. Krishna Rao joined Anthropic before anyone believed the number.
2. Krishna Rao watched a company grow past reason in months.
3. Krishna Rao helped raise billions nobody thought were coming.

**Andrej Karpathy — most people aren't really using AI (3.2M views)**
1. Andrej Karpathy says your ChatGPT subscription is wasted.
2. Andrej Karpathy found the real gap. It isn't access.
3. Andrej Karpathy says paying for AI isn't the same as using it.

### UNCONFIRMED source flags
Four of the nine new clips carry UNCONFIRMED source attribution (original interview name not captured in the repost caption): the Karpathy clip, one of the five Dario clips (3-hour podcast), the Dario Congressional-testimony clip (exact hearing unconfirmed), and the Demis Hassabis clip. Views and speaker identity are verified; only the original episode/podcast name is unconfirmed. Do not fabricate a source name when captioning these — credit the repost handle only until confirmed.

### Apify quota status
No quota, auth, or billing errors encountered this run (`api-ninja/x-twitter-advanced-search`). All runs SUCCEEDED.

## 2026-07-24 — theaiaxon dedup goes live (STEP 1b); discovery comes up dry

**Backlog status at run start:** 28/100 available, 6 review. Well short of the 90-alert threshold.

**@theaibolt resweep:** `apify/instagram-reel-scraper` {"username":["theaibolt"],"resultsLimit":200} returned 143/143 items, byte-for-byte the same shortcode set as the last sweep. Zero new posts, zero pruning needed.

**@theaiaxon dedup (STEP 1b) — run for the first time with live data:**
- `apify/instagram-reel-scraper` on @theaiaxon returned exactly **1 published reel**: a Sam Altman / Tucker Carlson Show clip about whether ChatGPT can tell a curious teen from a kid in crisis (posted 2026-07-23, shortcode `DbJvmxvPYPD`).
- `getScheduledPosts` (Metricool brandId 6566296, America/Chicago, 2026-06-24→2026-08-23) returned **0 scheduled posts**.
- Neither call errored — dedup this run is CLEAN, not a fallback state.
- The Sam Altman/Tucker Carlson/ChatGPT-child-safety speaker+topic combo did not match any existing backlog candidate or clips_log entry, so nothing was pruned. It's now recorded in `data/backlog.json` under `theaiaxon_published_exclusions` so it's never resourced from a different repost URL in a future run.

**Discovery (available < 100, topped up attempt):** widened the net into speakers and fields not covered by prior sweeps:
- X/Twitter (`api-ninja/x-twitter-advanced-search`, Top results, viral engagement filter, video media): Ilya Sutskever, Yann LeCun, Bill Gates, Peter Thiel, "doctor AI diagnosis interview", "lawyer AI replace interview".
- Instagram (`data-slayer/instagram-search-reels`): Andrew Ng, musician AI, economist AI jobs, Fei-Fei Li, athlete AI training.

**Result: zero net-new qualifying clips.** All 11 actor runs SUCCEEDED (no quota/auth errors — this is a clean empty result, not a quota block). Every candidate reviewed failed at least one hard gate:
- Under the 1M-view line (most Fei-Fei Li, Andrew Ng, and athlete-AI results topped out in the tens or hundreds of thousands).
- No actual video attached — several of the highest "views" numbers on X (e.g. a 1.99M-view Marc Andreessen/Rogan thread by @cyrilXBT) turned out to be text/quote-tweet commentary summarizing an interview, not the interview clip itself.
- Format/spoken-words failures — e.g. a 2.19M-view UBI explainer (@artificialintelligenceee) has no on-camera named speaker, just narration over stock footage.
- Closest near-miss: an Andrew Ng bio-explainer reel at 984K views (@rabbitt.learning) — just under the gate, and it's a narrated biography montage rather than him speaking directly.

This confirms the account/speaker exhaustion pattern flagged 2026-07-09 and 2026-07-22 now extends to this wider set of untried Tier 2/3 names and cross-industry fields (medicine, law, music, economics, sports). Backlog remains **28/100 available** — unchanged from run start. No BACKLOG NEAR CAP alert warranted.

### Recommendation for future runs
1. Priority-1 lever still untried: mining the full source interview behind each of theaibolt's 143 posts for other 1M+ moments from the same episodes.
2. Per the 2026-07-09 STATUS note, consider surfacing the existing 500K-1M "review"-bucket clips for a user decision on relaxing the 1M gate — do not relax it silently.
3. @theaiaxon's own posting cadence (1 post/day-ish) means STEP 1b dedup should stay cheap going forward; no issues with the new step.

### Apify quota status
No quota, auth, or billing errors encountered this run (`apify/instagram-reel-scraper` x2, `getScheduledPosts` x1, `api-ninja/x-twitter-advanced-search` x6, `data-slayer/instagram-search-reels` x5). All 13 calls SUCCEEDED.

## 2026-07-24 — Daily discovery run (3 parallel lanes: X search, IG cross-industry, mega-podcast recency)

**@theaibolt refresh:** Apify `apify/instagram-reel-scraper` sweep (200-result limit, 142/143 items returned) found **zero new posts** since the last sweep, identical to the 2026-07-22 sweep. No pruning needed.

**@theaiaxon dedup (STEP 1b, the never-repost loop):** scraped @theaiaxon's own published reels (`apify/instagram-reel-scraper`, 1 result — the account has posted exactly once so far: Sam Altman / Tucker Carlson Show on ChatGPT child safety, not a match to anything in the backlog) and pulled Metricool scheduled posts for brand 6566296 across a 60-day window (0 scheduled, call succeeded with no errors). Dedup is fully clean this run — no matches, nothing pruned, no errors on either source.

**Data-quality correction:** the stored `available_count` field said 34, but only 28 of the 34 existing candidates actually carried `status: "available"` (6 were `status: "review"`). Recounted directly from the candidates array; this field will be kept accurate going forward.

**Discovery (28 available, well short of 100 — topped up):** ran 3 parallel subagent lanes —
1. X/Twitter search (`apidojo/tweet-scraper`) across Tier 2/3 AI researchers, contrarians, and cross-industry queries — strong yield on named AI figures, weak/noisy on cross-industry non-tech terms.
2. Instagram cross-industry keyword search (`data-slayer/instagram-search-reels`) targeting doctors, lawyers, athletes, chefs, teachers, farmers, clergy, and Hollywood figures discussing AI.
3. Mega-podcast recency check (14 accounts: Rogan, DOAC, Lex Fridman, All-In, Shetty, Impact Theory, Howes, Ferriss, Vaynerchuk, Huberman, Modern Wisdom, 20VC, Diamandis, Mostly Human) — only checking posts newer than the 2026-07-09 exhaustion date, per standing guidance not to re-sweep exhausted lists.

**Result:** +21 clean additions to `available`, +1 flagged to `review` (Tom Holland — 37.7M views but only 7s, borderline format). No Apify quota/auth errors on any of the 3 lanes — `@tferriss`, `@modernwisdompodcast`, and `@20vc` failed to resolve (private/wrong handle), which is a per-account data issue, not a quota block.

Backlog now **49/100 available** (was 28), **7 review** (was 6). Genuine cross-industry (non-tech, non-CEO) 1M+ content remains scarce on both platforms — confirmed independently by 2 of the 3 subagents, not a tooling gap. Still well short of the 90-alert threshold.

### New additions (available) — top 10 by views

| Speaker | Views | Field | Source | Pillar | URL |
|---|---|---|---|---|---|
| Ray Kurzweil | 36,194,164 | Futurist | Joe Rogan Experience | Controversial | https://x.com/KanekoaTheGreat/status/1767631628917248346 |
| Roman Yampolskiy | 30,192,813 | AI safety research | Lex Fridman Podcast | Controversial | https://x.com/lexfridman/status/1797383905034514684 |
| Pope Leo XIV | 4,815,121 | Religion | Vatican News | Educational | https://www.instagram.com/reel/DJeUf3Utxyo/ |
| Mustafa Suleyman | 7,456,038 | AI/Tech (Microsoft AI) | Financial Times | Controversial | https://x.com/FT/status/2021913057065160828 |
| Ray Kurzweil | 8,274,721 | Futurist | Joe Rogan Experience | Controversial | https://x.com/TheChiefNerd/status/1767712511581643244 |
| Bill Gates | 3,769,484 | Tech/Philanthropy | Unconfirmed | Controversial | https://x.com/EndWokeness/status/1840738265839685868 |
| Ilya Sutskever | 3,094,692 | AI research (SSI) | Univ. of Toronto convocation | Educational | https://x.com/Yuchenj_UW/status/1931883302623084719 |
| Peter Thiel | 3,338,850 | Venture Capital | Unconfirmed | Controversial | https://x.com/jawwwn_/status/2026688379207753995 |
| Bill Gates | 3,006,175 | Tech/Philanthropy | Tonight Show (NBC) | Controversial | https://x.com/redpillb0t/status/2040397754476999075 |
| Fran Drescher | 2,848,457 | Acting/SAG-AFTRA | NBC LA | Controversial | https://www.instagram.com/reel/DPP1sDeCbRz/ |

Pillar mix this batch again skewed Controversial (13 of 21 available adds) with Educational 6, Inspirational 2, Emotional 0 — future sourcing should keep targeting Educational/Inspirational picks to rebalance toward the page's target mix.

### Flagged to review (not promoted — need manual confirmation)

| Speaker | Views | Reason | URL |
|---|---|---|---|
| Tom Holland | 37,699,926 | Only 7s (quip, not a full segment); credited via a repost account, not the original publisher | https://www.instagram.com/reel/DZp6OfjM-YV/ |

### Dropped as non-qualifying (found but not added)

- Dario Amodei, WEF panel clip, 1.2M views — already 5 clips deep in the backlog for this speaker, weak differentiation, lowest view count of the batch.
- Bill Gates, 3rd clip found this run (storiesuntoldour repost) — near-duplicate topic of the Tonight Show clip above, dropped to avoid tripling this speaker.
- Jeremy Greene reaction video, 10.3M views — not a mainstream public figure, format is a reaction clip rather than an interview.
- Jessica Reid classroom-AI-tools clip, 2.9M views — listicle/tutorial format, explicitly excluded by the FORMAT criterion.
- Unconfirmed-speaker clip via @artificialintelligenceee (Honestly podcast jailbreak segment), 1.6M views — could not confirm who is speaking.

### Hooks for top 3 new additions

**Ray Kurzweil — AGI by 2029 on Joe Rogan (36.2M views)**
1. Ray Kurzweil made this AI prediction in 1999. It is still on track.
2. Ray Kurzweil named the year machines catch up to us.
3. Ray Kurzweil has one AI date circled. Joe Rogan pushed back hard.

**Roman Yampolskiy — 99.9999% AGI risk on Lex Fridman (30.2M views)**
1. Roman Yampolskiy put a number on how AI ends us.
2. Roman Yampolskiy gave Lex Fridman a number nobody wants to hear.
3. Roman Yampolskiy is almost certain about one AI outcome. Almost.

**Pope Leo XIV — AI and the industrial revolution (4.8M views)**
1. Pope Leo XIV picked his name because of AI.
2. Pope Leo XIV compared AI to a crisis from 1891.
3. Pope Leo XIV chose his name to answer a machine.

### Apify quota status
No quota, auth, or billing errors encountered across any of the actor runs this session (`apify/instagram-reel-scraper`, `apidojo/tweet-scraper`, `data-slayer/instagram-search-reels`). All runs SUCCEEDED; the only failures were per-account resolution issues (private/renamed handles), not platform-wide limits.

## 2026-07-24 — Run #4: dedup + 4-lane discovery (+10 available, +1 review, 0 pruned)

**@theaibolt refresh:** `apify/instagram-reel-scraper` sweep (200-limit, 143/142 items returned) — zero new posts vs the known 143-URL posted history. No pruning needed.

**@theaiaxon dedup (STEP 1b):** Apify published-reels scrape (100-limit) still returns exactly 1 published reel — Sam Altman / Tucker Carlson teen-safety clip, already tracked in `theaiaxon_published_exclusions`. Metricool `getScheduledPosts` (brandId 6566296, 2026-06-24 to 2026-08-23, America/Chicago) returned 0 scheduled posts. Both checks succeeded with no errors — dedup is clean and complete this run.

**Backlog before this run:** 49/100 available, 7 review. Below the 100 target, so discovery ran.

**Discovery — 4 parallel subagent lanes:**
1. X-search, Tier 2/3 AI researchers/execs (Gary Marcus, Stuart Russell, Kai-Fu Lee, Fei-Fei Li, Timnit Gebru, Eliezer Yudkowsky, Jan Leike, Jared Kaplan, Chris Olah, Emad Mostaque, Percy Liang, Arthur Mensch, Clement Delangue, Aidan Gomez, Noam Shazeer, Reid Hoffman, Vinod Khosla, Satya Nadella, Sundar Pichai, Sam Altman non-Tucker-Carlson topics) — **5 qualifiers**: 3 fresh Sam Altman topics + Stuart Russell + Connor Leahy. Everyone else on the list came back empty.
2. X-search, cross-industry non-tech AI voices (entertainment, sports, comedy, medicine/law, world leaders, non-AI-native CEOs) — **1 qualifier**: Alexandria Ocasio-Cortez. Mark Cuban had 2 tweets over 1M views but no attached video (text/link cards) — excluded on the FORMAT gate, not silently dropped.
3. Instagram mega-podcast recency check (13 accounts, posts newer than 2026-07-14) — **0 qualifiers**. Confirms the 2026-07-09 exhaustion finding still holds. Found and corrected 3 renamed/broken handles: `@tferriss`→`@timferriss`, `@modernwisdompodcast`→`@chriswillx`, `@nikhilkamathofficial`→`@nikhilkamathcio` (all checked, all empty). `@20vc` remains unresolvable after 5 handle variants tried.
4. X-search, finance/entertainment figures (Raoul Pal, Cathie Wood, Ray Dalio, Chamath Palihapitiya, Jamie Dimon, Larry Fink, Michael Burry, Jim Cramer, Warren Buffett, Arnold Schwarzenegger, Snoop Dogg, MrBeast, Oprah Winfrey) — **5 results** (4 qualifiers + 1 review): Cathie Wood, Ray Dalio, Jamie Dimon, Larry Fink qualified; Snoop Dogg flagged to review (views right at the 1,001,550 floor and AI voice-cloning is a secondary angle within a broader Drake/Kendrick-beef story). Michael Burry's AI-bubble clips were all narrator/text-card videos, not him on camera — excluded on FORMAT, not silently dropped.

**Net result:** +10 available, +1 review, 0 pruned. **Available now 59/100** (was 49), review 8.

Pillar mix this batch: Controversial 5 (Cathie Wood, Larry Fink, AOC, Connor Leahy, +Snoop Dogg in review), Educational 3 (Stuart Russell, Ray Dalio, Sam Altman/competitive-coding), Inspirational 2 (Sam Altman/no-equity, Jamie Dimon), Emotional 1 (Sam Altman/GPT-5 reaction). Still Controversial-heavy overall across the full backlog; keep prioritizing Educational/Inspirational sourcing in future runs.

### New additions this run

| Speaker | Views | Dur | Date | Topic | URL |
|---|---|---|---|---|---|
| Sam Altman | 29,275,565 | ? | 2024-12-17 | No equity in OpenAI, does it for love | https://x.com/teslaownersSV/status/1868894670476239164 |
| Sam Altman | 5,664,615 | ? | 2025-07-23 | First reaction testing GPT-5 | https://x.com/ChrisGPT/status/1948096257483763798 |
| Cathie Wood | 7,040,744 | 43s | 2025-08-03 | Tesla as largest AI project, $8-10T robotaxi thesis | https://x.com/niccruzpatane/status/1951831193596404160 |
| Stuart Russell | 3,306,002 | ? | 2024-07-31 | AI is a black box, no nuclear-style safety guarantees | https://x.com/ControlAI/status/1818748081589846023 |
| Ray Dalio | 3,005,360 | 2516s (full ep) | 2025-02-21 | AI's economic impact, debt crisis | https://x.com/TuckerCarlson/status/1893045548459954510 |
| Larry Fink | 2,778,942 | 84s | 2026-05-25 | AI data centers funded by pensions/savings | https://x.com/ShadowofEzra/status/2058718603633918343 |
| AOC | 1,972,067 | 47s | 2026-05-21 | Contaminated water near a Meta AI data center | https://x.com/krassenstein/status/2057533802495549789 |
| Jamie Dimon | 2,132,369 | 16s | 2026-05-16 | AI enables 3.5-day work weeks, longer lifespans | https://x.com/MarioNawfal/status/2055652992460697812 |
| Sam Altman | 1,399,517 | ? | 2025-02-08 | Internal model ranked 50th-best competitive programmer | https://x.com/tsarnick/status/1888111042301211084 |
| Connor Leahy | 1,106,441 | ? | 2023-05-02 | AI extinction risk, on Amanpour & Co | https://x.com/amanpour/status/1653452034463367168 |

### Flagged to review (not promoted — need manual confirmation)

| Speaker | Views | Reason | URL |
|---|---|---|---|
| Snoop Dogg | 1,001,550 | Views right at the 1M floor; AI voice-cloning is a secondary angle inside a broader Drake/Kendrick-beef story, not the central topic | https://x.com/itsavibe/status/1796268440136593603 |

### Dropped as non-qualifying (found but not added)

- Mark Cuban, 2 tweets (1.12M and 932K views) on AI disrupting small business — no attached video, link/text cards only, fails the FORMAT hard gate.
- Michael Burry, several 1M+ view AI-bubble tweets — all narrator/graphics-over-stock-footage videos, not Burry speaking on camera, fails FORMAT.
- Chamath Palihapitiya, Joe Rogan repost on AI — only 143,546 views, below the 1M gate.

### Hooks for top 3 new additions

**Sam Altman — no equity in OpenAI (29.3M views)**
1. Sam Altman just admitted he owns zero OpenAI stock.
2. Sam Altman does not own a single share of OpenAI.
3. Sam Altman gave up equity most people would kill for.

**Sam Altman — first reaction testing GPT-5 (5.7M views)**
1. Sam Altman tested GPT-5 himself. It stunned even him.
2. Sam Altman asked GPT-5 his hardest question. It just knew.
3. Sam Altman built GPT-5. It still caught him off guard.

**Cathie Wood — Tesla as the largest AI project (7.0M views)**
1. Cathie Wood says Tesla is not a car company anymore.
2. Cathie Wood puts a ten trillion dollar number on this.
3. Cathie Wood thinks robotaxis change everything. Here is her math.

### Apify quota status
No quota, auth, or billing errors encountered across any of the 4 subagent lanes or the theaibolt/theaiaxon dedup sweeps (`apify/instagram-reel-scraper`, `apidojo/tweet-scraper`, `apify/rag-web-browser`). All runs SUCCEEDED; the only failures were per-account handle resolution issues (renamed/private/unresolvable accounts), not platform-wide limits.

## 2026-07-25 — Daily discovery run (X/Twitter, 4-lane parallel)

**@theaibolt refresh:** Apify `apify/instagram-reel-scraper` full sweep (200-result limit, 143/143 items returned) found **zero new posts** since the last sweep — posted_urls list unchanged, no pruning needed.

**@theaiaxon dedup (STEP 1b):** Apify published-reels scrape now returns 2 published items (was 1). The Sam Altman / Tucker Carlson post was already tracked. A NEW post surfaced: Joe Rogan / Duncan Trussell discussing the "Ghost Murmur" alleged CIA AI+quantum-magnetometry heartbeat surveillance claim (Joe Rogan Experience #2481, published 2026-07-24). Metricool `getScheduledPosts` (brandId 6566296, -30/+30 day window, America/Chicago) returned 1 item — an Elon Musk / Dwarkesh Patel post using the HAL 9000 "it didn't malfunction, it optimised" analogy for AI safety — but its status was already `PUBLISHED`, not future-scheduled (live at https://www.instagram.com/reel/DbL8iQzEtO1/). Both new items were checked against the backlog by speaker+topic: **no matches found, no pruning triggered.** Both new exclusions were added to `theaiaxon_published_exclusions` for future runs. Both dedup checks succeeded cleanly, no errors — this run is fully deduped.

**Discovery (available 59 < 100, topped up):** 4 parallel subagent lanes:
1. X search — Tier 1/2 speakers with fresh angles not yet in the backlog (Bezos, Ellison, Zuckerberg, plus re-checks of Tim Cook/Nadella/Pichai)
2. X search — cross-industry non-tech voices (world leaders, entertainers, athletes, intellectuals, doctors, business figures outside tech)
3. Instagram theme-page recency check (13 accounts, posts after 2026-07-09 only)
4. X search — finance/entertainment/global figures

Lane 3 (IG theme pages) found **zero new qualifiers** — confirms the FORMAT-gate exhaustion from prior runs: @airesearches and @evolving.ai are now 100% AI-generated/CGI content post-2026-07-09, @ai_wealth is a dead handle (`not_found` error), @aitherevolution remains mis-resolved to unrelated accounts. Both need manual handle correction before the next IG sweep.

Lanes 1, 2, and 4 (X search) were the productive levers: **+12 available**, review count unchanged at 8.

New speakers/topics added:
- **Larry Ellison** (brand-new speaker, 4 distinct topics: AI police-surveillance system, Stargate Project cancer-vaccine framing, nuclear-powered GPU clusters, AI commoditization/data-moat argument) — highest single-speaker yield this run, space out when scheduling.
- **Ken Griffin** (Citadel CEO, 2 topics likely from the same underlying Stanford-style talk — space apart if both scheduled): AI automating "extraordinarily high-skilled" finance-PhD work in days, and a step-change in internal AI productivity.
- **Theo Von** and **Jeff Bridges** (same podcast episode, This Past Weekend w/ Theo Von — source confirmed): Von on AI data centers and a coming "emotional credit score"; Bridges on using Suno AI to write a song for his wife.
- **Jeff Bezos** — tech disruption creates invisible new jobs analogy.
- **Mark Zuckerberg** — new topic (AI-driven erosion of human social connection), distinct from the existing stale 2023 Metaverse-avatar clip.
- **Emmanuel Macron** — first world-leader speaker in the backlog (Mistral AI / European AI sovereignty).
- **Billie Eilish** — highest views this run (12.8M), reacting on-camera to an AI deepfake Met Gala photo of herself.

Most new adds are `source: UNCONFIRMED` (X repost metadata rarely names the underlying event/venue) — verify at edit time before posting; Theo Von/Jeff Bridges are the two `confirmed`-source exceptions.

Tried-and-empty this run (do not re-search next time unless noted): Tim Cook, Satya Nadella, Sundar Pichai; Xi Jinping, Narendra Modi, Justin Trudeau, Zelensky, JD Vance, Gavin Newsom, Rishi Sunak; Zendaya, Timothee Chalamet, Dwayne Johnson, Kevin Hart, Ryan Reynolds, Ariana Grande, Nicki Minaj, Kanye West; Djokovic, Ronaldo, Messi, Belichick, Saban; Yuval Noah Harari (695K, just under gate), Gladwell, Jordan Peterson, Sam Harris; Peter Attia, Huberman, Eric Topol; Bernard Arnault, Mukesh Ambani, Howard Schultz; Bill Ackman, Druckenmiller, David Sacks, Bill Hwang, Taleb, El-Erian, Larry Summers; Andrew Schulz, Whoopi Goldberg, The View, Piers Morgan, Megyn Kelly, King Charles, MBS, Tom Brady, Bill Maher.

**No Apify quota or auth errors** across any of the 4 discovery lanes or the theaibolt/theaiaxon refresh calls.

**Available now 71/100** (was 59), review 8 (unchanged).

### Top 3 new additions — hooks

**Billie Eilish** (12,840,342 views, Controversial)
1. Billie Eilish saw a fake AI photo of herself. Her reaction shocked fans.
2. Billie Eilish got blamed for an outfit she never wore. AI made it up.
3. Everyone thought it was Billie Eilish. It was actually AI. She had one thing to say.

**Ken Griffin** (6,494,151 views, Emotional)
1. Ken Griffin watched AI finish months of work in days. Then he went home depressed.
2. Ken Griffin runs a top hedge fund. Watching his own AI made him uneasy.
3. Ken Griffin saw what AI can now do to skilled jobs. It changed his mood.

**Theo Von** (4,576,513 views, Controversial)
1. Theo Von warns one company could soon own everyone's personal data forever.
2. Theo Von thinks AI is building something nobody asked for near their home.
3. Theo Von predicts a score that follows you everywhere. AI decides it.

### UNCONFIRMED flags
Source venue/event unconfirmed for: Jeff Bezos, all 4 Larry Ellison clips (2 likely Oracle CloudWorld 2024, exact confirmation pending), Mark Zuckerberg, both Ken Griffin clips, Emmanuel Macron, Billie Eilish. Verify before posting.

## 2026-07-26 — Daily discovery run (3-lane parallel: X new-speakers, cross-industry, YouTube-native)

**@theaibolt refresh:** Apify `apify/instagram-reel-scraper` full sweep (200-result limit, 143/143 items returned) found **zero new posts** — newest timestamp still 2026-07-09. @theaibolt has not posted anything new in 17 days; this lever remains fully exhausted.

**@theaiaxon dedup (STEP 1b):** Apify published-reels scrape now returns 4 published items (was 2). The 2 already-tracked items (Sam Altman/Tucker Carlson; Joe Rogan/Duncan Trussell "Ghost Murmur") are unchanged. 2 NEW published posts surfaced:
- **Raoul Pal / Diary of a CEO** — "AI can copy any business and build a better version in minutes" (published 2026-07-26)
- **Palmer Luckey / Joe Rogan Experience #2394** — battlefield AI "hive mind" system (Ghost X drone, shared real-time view for soldiers/drones/robots) (published 2026-07-25)

Metricool `getScheduledPosts` (brandId 6566296, -30/+30 day window, America/Chicago) returned only the already-tracked Elon Musk/Dwarkesh HAL-9000 post (still `PUBLISHED`, not a new future-scheduled item) — **no new scheduled posts.** Both new exclusions checked against the backlog: Raoul Pal was not present (no pruning). The 2 existing Palmer Luckey backlog clips (jailbreak-ChatGPT; "software engineering problem" framing of warfare) cover distinct topics from the newly-excluded hive-mind clip, even though all three trace to the same JRE #2394 episode — kept as available, flagged for a manual same-episode overlap check before scheduling. Both new items added to `theaiaxon_published_exclusions`. **Both dedup checks succeeded, no errors — this run is fully deduped.**

**Discovery (available 71 < 100, topped up):** 3 parallel subagent lanes:
1. **Lane A** — X search for brand-new speakers not yet tried (Big Tech / VC-adjacent figures: LeCun, Palihapitiya, Calacanis, Schmidt, Chesky, etc.)
2. **Lane B** — X + Instagram search for cross-industry non-tech speakers (healthcare, law, education, sports execs, entertainment producers/directors, aviation, journalism, science, military, religion, chefs/tradespeople)
3. **Lane C** — YouTube-native search via `api-ninja/youtube-search-scraper` (backed by the YouTube Data API for authoritative view counts, since generic web search returned no reliable view data for YouTube pages)

**Lane B returned zero new qualifiers** after 9 successful Apify calls (~40 search terms plus IG keyword-reel sweeps) — a genuine exhaustion signal for the current cross-industry query set, not a quota issue. Near-misses checked and rejected: Neil deGrasse Tyson (~99K views, well under gate), Dalai Lama (topic was anger/compassion, not AI), Bill Maher/Kara Swisher (1.02M views but about Ozempic), David Friedberg (1.32M views but about US vs. socialism). No Apify quota or auth errors in this lane.

**Lanes A + C together yielded +16 available** — the best single-run haul since the 2026-07-09 account-audit exhaustion:
- **Yann LeCun** — 2nd topic (AI innovation shifting to India/Africa), distinct from the existing "doomers are wrong" clip.
- **Chamath Palihapitiya** — 3 topics (Tesla/Google as AI-race winners; reacting to AI-agent token costs; Tesla FSD safety gains). Heavy single-run yield for one speaker, space out.
- **Jason Calacanis** — Amazon "100% robotic by 2030" prediction.
- **Eric Schmidt** — 3 topics (booed at a commencement address over AI jobs; AI's "infinite" energy demand; a TED talk on AI's underestimated impact). 2 via X, 1 via YouTube — heaviest single-speaker yield this run, space out heavily.
- **Brian Chesky** — Airbnb's AI-driven "founder mode" vision.
- **Sundar Pichai** — 2 topics via YouTube (Bloomberg business interview; casual MKBHD product conversation) — first time this speaker cleared the bar after repeated X-search misses.
- **Satya Nadella** — Copilot+ PCs vs. Mac, via YouTube (WSJ) — first time clearing the bar.
- **Jordan Peterson** — AGI/super-intelligence conversation, via YouTube — first time clearing the bar.
- **Sam Altman** — landmark first Senate AI-regulation testimony, via YouTube — distinct from 3 existing Altman clips and the excluded Tucker Carlson theaiaxon post.
- **Tristan Harris** — 2nd topic (AI lab leaders privately prepping for societal collapse).
- **Yuval Noah Harari** — AI as the first technology able to make its own decisions, via YouTube — first time clearing the bar (prior X-search high was 695K; this native YouTube keynote clears at 2.58M).

**Key finding:** the YouTube lane (Priority 3, previously underused relative to X/IG) unlocked 3 speakers marked "tried-and-empty" on X in prior runs (Nadella, Peterson, Harari) — native YouTube view counts often run far higher than X-repost view counts for the same interview. Recommend YouTube search become a **standing 4th discovery lane** going forward, not just a fallback.

Tried-and-empty this run, cross-industry lane (do not re-search bare unless a genuinely new angle emerges): Neil deGrasse Tyson, Dalai Lama, Bill Maher, Kara Swisher, David Friedberg, Sal Khan, Rick Rubin, Gordon Ramsay, Daryl Morey, Billy Beane, Sanjay Gupta, Marty Makary, James Cameron, Christopher Nolan, will.i.am, Michio Kaku, Chris Hadfield, plus generic doctor/lawyer/teacher/chef/pilot/scientist/film-director keyword sweeps on Instagram (returned only AI-generated content-farm videos, failing the FORMAT gate).

**No Apify quota or auth errors** across any of the 3 discovery lanes or the theaibolt/theaiaxon refresh calls.

**Available now 87/100** (was 71), review 8 (unchanged). Below the 90-alert threshold — no cap alert this run.

### Top 3 new additions — hooks

**Chamath Palihapitiya — Tesla/Google as the AI-race winners (7,918,964 views)**
1. Chamath Palihapitiya named the two companies winning the AI race.
2. Chamath Palihapitiya says only two companies can truly win AI.
3. Chamath Palihapitiya ranked the AI race. Two names made the cut.

**Eric Schmidt — booed at commencement over AI jobs (1,251,131 views)**
1. Eric Schmidt got booed on stage. AI jobs was the reason.
2. Eric Schmidt talked AI at a graduation. Students booed him.
3. Eric Schmidt faced boos mid-speech while talking about AI jobs.

**Yuval Noah Harari — AI as the first self-deciding technology (2,583,142 views)**
1. Yuval Noah Harari says AI just crossed a line no tech has.
2. Yuval Noah Harari warns AI can now decide things on its own.
3. Yuval Noah Harari says history has never seen a technology like this.

### UNCONFIRMED flags
Source event/venue unconfirmed for: Jason Calacanis (Amazon prediction), Chamath Palihapitiya's Tesla-FSD clip and agent-token-cost clip (All-In episode confirmed as the poster, but not cross-verified), Eric Schmidt's energy-demand clip. Verify before posting. All YouTube-lane clips (Pichai x2, Nadella, Peterson, Altman, Harris, Schmidt TED, Harari) have source and view counts confirmed directly from YouTube via the API-backed scraper.

## 2026-07-26 (addendum) — Bulletproof live re-verification pass (user-requested)

User asked for certainty beyond point-in-time discovery captures: that every "available" backlog clip genuinely has 1M+ views *right now*, and that none duplicate @theaibolt's posted library.

**Method:** re-fetched live metadata for all 87 then-available candidates directly from source, split by platform:
- **YouTube (8 clips)** — `beyondops/youtube-metadata-scraper-pro-v2`, direct video URL lookup. All 8 reconfirmed ≥1M, numbers essentially unchanged.
- **Instagram (24 clips)** — `data-slayer/instagram-post-details`, direct post URL lookup (`metrics.play_count`). All 24 reconfirmed ≥1M.
- **X/Twitter (55 clips)** — several actors tried first: `apidojo/tweet-scraper` with `startUrls` returned 0 items (doesn't support direct tweet-URL lookup here); `kaitoeasyapi/twitter-x-data-tweet-scraper` with `tweetIDs` failed outright; `apidojo/tweet-scraper` with `conversationIds` worked but returns the entire reply thread (300+ items per tweet) rather than just the root tweet, unworkably expensive at 55x scale. Landed on `danek/twitter-scraper` with `lookup_post_ids` — clean, direct, one row per requested tweet ID, no thread noise. Ran all 55 in a single batch call.

**Result: 86/87 reconfirmed live at 1,000,000+ views**, all within normal natural-growth drift of their recorded values (no decreases observed, consistent with view counts being monotonic). **1 exception:** the Bill Gates / @redpillb0t clip (`x.com/redpillb0t/status/2040397754476999075`, recorded 3,006,175 views) returned an access error ("content may be private, deleted, or app-only") on two independent methods — the direct `danek/twitter-scraper` lookup and, separately, a sub-agent's `rag-web-browser` check. **Downgraded from `available` to `review`** pending a manual check; cannot currently confirm it clears the 1M gate or is even still live.

**@theaibolt exact-URL dedup:** cross-checked all 87 backlog URLs against @theaibolt's same-day freshly-scraped 143-post library (URL-exact match). **Zero matches.** Note: per this project's dedup_semantics, matching @theaibolt by *speaker+topic* is actually expected and even prioritized (their library is a source catalog we deliberately repost proven clips from) — the binding "never repost" constraint is @theaiaxon's own published+scheduled history, which was already checked clean earlier in today's run (STEP 1b).

**Available now 86/100** (was 87 before this pass), review 9 (was 8).

## 2026-07-27 — Daily discovery run (3-lane parallel: X new-speakers, YouTube-native, theme-page recency), backlog hit the 100 cap

**@theaibolt refresh:** Apify `apify/instagram-reel-scraper` full sweep (200-result limit, 143/143 items returned, exact URL-set match against the stored posted_urls) found **zero new posts** — @theaibolt has not posted anything new since 2026-07-09, now 18 days. This lever remains fully exhausted.

**@theaiaxon dedup (STEP 1b):** Apify published-reels scrape now returns 5 published items (was 4). 1 NEW published post surfaced:
- **Jeff Bezos / America Business Forum** — "AI reviews building permits in 10 seconds instead of months" (published 2026-07-26, Miami stage appearance)

Checked against the backlog: no match, no pruning needed — but notably, this run's own Lane A (X search) independently surfaced an X repost of the exact same Bezos permit clip; it was caught and excluded before ever entering the backlog (see dedup section below). Metricool `getScheduledPosts` (brandId 6566296, 2026-06-27 to 2026-08-26 window, America/Chicago) returned only the already-tracked Elon Musk/Dwarkesh HAL-9000 post (still `PUBLISHED`) — **no new scheduled posts.** New exclusion added to `theaiaxon_published_exclusions`. **Both dedup checks succeeded, no errors — this run is fully deduped.**

**Discovery (available 86 < 100, topped up):** 3 parallel subagent lanes:
1. **Lane A** — X/Twitter search for new speakers across tech/VC, entertainment, sports, music, and health
2. **Lane B** — YouTube-native search (now a standing lane per 2026-07-26's recommendation)
3. **Lane C** — theme-page recency check on @evolving.ai, @theaifield, @theaipage, @airesearches, @ainterestingupdate, @godofprompt, @power.ai, @artificialintelligenceee, @thewizeai, @chatgptricks — restricted to posts after 2026-07-22 (the date of the last exhaustive sweep)

**Lane C returned zero qualifiers.** @thewizeai and @chatgptricks errored (empty/private data). Of 54 posts returned across the other 8 accounts, only 5 cleared 1M+ views for the post-07-22 window, and all 5 failed the hard FORMAT gate: two AI-generated anime recreations ("Naruto vs Pain", "Baki"), an AI dystopia short film, a humanoid-robot fight-league clip, and a no-speaker iFLYTEK product demo. Consistent with this batch of theme pages skewing CGI/no-speaker content.

**Lanes A + B together yielded 19 new qualifying URLs** after dedup. 4 raw duplicates were caught and discarded:
- Jeff Bezos (Miami permits, X repost) — matches the new @theaiaxon published exclusion above
- Jeff Bezos (farmer-to-massage-therapist analogy) — exact URL already in the backlog since 2026-07-25
- Marc Andreessen ("AGI already quietly crossed") — same speaker+topic already in the backlog since 2026-07-24
- Tristan Harris (Alibaba AI safety incident) — same speaker+topic already in the backlog

Since only 14 were needed to reach the 100 cap, the 14 highest-confidence, most pillar-balanced candidates were promoted to `available`; the remaining 5 were kept as `review` — all are clean 1M+ qualifiers, held back purely because of the cap:
- Molly Crabapple (60 Minutes, AI art scraping) — Controversial, 1.14M
- Sen. Bernie Sanders (interviewing Claude on AI privacy) — Controversial, 4.9M
- Sasha Luccioni (TED, AI ethics) — Controversial, 1.95M, age-flagged (2023)
- Andrew Yang (CNBC, AI and jobs) — Educational, 1.05M, age-flagged, lowest views this run
- Demis Hassabis 2nd topic (Davos AGI debate w/ Dario Amodei, via re-upload) — Educational, 1.08M, weakest sourcing this run

**Promote these 5 first next run, before new discovery.**

**New speakers unlocked this run:** Bill McDermott (ServiceNow CEO, CNBC), Chris Olah (Anthropic co-founder, addressed the Pope at the Vatican — distinct from saturated Dario Amodei), David Sacks (a16z, White House AI Czar), Murphy Campbell (independent musician, AI song-cloning harm story — fills the Emotional pillar), Gary Brecka (health/longevity), Matthew McConaughey with Timothee Chalamet (Oscars/AI-acting), Adam Silver (NBA Commissioner, AI officiating review), Joseph Gordon-Levitt (Utah Capitol AI child-safety testimony), Roman Yampolskiy (AI safety researcher), Ian Bremmer (geopolitical risk), Rishi Sunak (former UK PM, Davos panel). Also added distinct 2nd topics for already-present speakers Mustafa Suleyman (TED talk), Jensen Huang (NVIDIA GTC 2026 keynote — 35.9M views, largest single view count surfaced this run), and Andrej Karpathy (Lex Fridman #333, Tesla AI).

**No Apify quota or auth errors** across any of the 3 discovery lanes or the theaibolt/theaiaxon refresh calls.

**BACKLOG NEAR CAP: 100/100 1M+ clips found - review or raise the cap.** Available now 100/100 (was 86), review 14 (was 9, +5 surplus). Alert threshold (90) exceeded — the pool is now completely full for the first time.

### Top 3 new additions — hooks

**Roman Yampolskiy — which jobs survive AI by 2030 (20,313,086 views)**
1. Roman Yampolskiy says most jobs will not survive past 2030.
2. Roman Yampolskiy picked the jobs AI cannot touch. Most failed.
3. Roman Yampolskiy ranked every job by how long it survives AI.

**David Sacks — the real AI danger isn't robots (16,352,654 views)**
1. David Sacks says the real AI danger is not robots.
2. David Sacks named the AI risk nobody is talking about.
3. David Sacks thinks the scariest AI outcome has nothing to do with robots.

**Jensen Huang — NVIDIA GTC 2026 keynote (35,952,926 views)**
1. Jensen Huang revealed what powers AI next. It shocked the room.
2. Jensen Huang unveiled NVIDIA's next AI move live on stage.
3. Jensen Huang showed the future of AI. Few saw it coming.

### UNCONFIRMED flags
Source not independently verified beyond the repost account for: Murphy Campbell (AI song-cloning story — originating platform/interview unconfirmed), Joseph Gordon-Levitt (local Utah news source names bill HB286, lends credibility, but not cross-checked further). Several Lane A candidates carry estimated (not scraper-confirmed) durations since the source actor doesn't expose exact runtime for reposted X clips — flagged individually in their `note` fields. Verify all of the above before scheduling.

## 2026-07-27 (addendum) — Second same-day invocation, verification-only pass

This scheduled run fired again ~5.5 hours after the run above (10:26 UTC -> 15:57 UTC), which had already topped the backlog to the 100/100 cap and pushed to main. No fresh discovery was warranted (cap already met, `available_count` == 100).

Re-ran STEP 1b (the bulletproof @theaiaxon dedup check) as a live guard: Apify published-reels scrape for @theaiaxon returned the same 5 published items as the run above (Palmer Luckey/Rogan, Duncan Trussell/Rogan Ghost Murmur, Jeff Bezos permits, Sam Altman/Tucker Carlson, Raoul Pal/Diary of a CEO), all already recorded in `theaiaxon_published_exclusions`. Metricool `getScheduledPosts` (brandId 6566296, 2026-06-27 to 2026-08-26, America/Chicago) returned only the same Elon Musk/Dwarkesh HAL-9000 post, status `PUBLISHED`, already excluded. No new published or scheduled posts, no matches against the backlog, nothing to prune.

No discovery run, no backlog/found_clips changes. Backlog remains 100/100 available, fully deduped.

## 2026-07-28 — Run #8: dedup-driven prune + backfill from review pool (no new discovery needed)

**@theaibolt refresh:** Apify `apify/instagram-reel-scraper` full sweep (200-result limit, 143/143 items returned, exact URL-set match) found **zero new posts** — max timestamp across all 143 items is still 2026-07-09T04:38:51Z. 19 days of continued exhaustion; this lever remains fully dead.

**@theaiaxon dedup (STEP 1b):** Apify published-reels scrape now returns 7 published items (was 5). 2 NEW published posts surfaced since the 2026-07-27 run:
- **Dario Amodei / CBS News** — Pentagon asked Anthropic to drop no-spying/no-autonomous-weapons limits from its defense contract; Amodei refused, Trump ordered agencies to stop using Anthropic, Hegseth labeled it a supply-chain risk (published 2026-07-27)
- **Geoffrey Hinton / 60 Minutes** — Scott Pelley asks if humans will become the second most intelligent species on the planet; Hinton says "yeah" (published 2026-07-27)

Metricool `getScheduledPosts` (brandId 6566296, 2026-06-28 to 2026-08-27 window, America/Chicago) returned only the already-tracked Elon Musk/Dwarkesh HAL-9000 post (still `PUBLISHED`) — **no new scheduled posts.** Both new items added to `theaiaxon_published_exclusions`. **Both dedup checks succeeded, no errors — this run is fully deduped.**

**Pruning (STEP 2):** Both new @theaiaxon posts matched existing backlog candidates by speaker+topic:
- Dario Amodei/CBS Pentagon story matched `twitter.com/r0ck3t23/status/2027698383037591957` (same Pentagon/Anthropic supply-chain-risk story, sourced via The Economist instead of CBS) — **pruned, status -> posted**
- Geoffrey Hinton/60-Minutes matched `reel/DN1KONh3q8z` (same 60 Minutes interview, same AI-surpasses-human-intelligence topic) — **pruned, status -> posted**

Available dropped to 98/100.

**Backfill (no new discovery run):** per the 2026-07-27 run's own recommendation to promote surplus `review` candidates before spending new Apify discovery quota, promoted the 2 highest-confidence review-surplus candidates back to `available`:
- **Bernie Sanders** — interviewing Claude directly on AI data privacy/surveillance (official Senate YouTube channel, 4,906,643 views, no age flag)
- **Molly Crabapple** — calls AI art scraping "the greatest art heist in history" (official 60 Minutes/CBS account, 1,142,612 views, no age flag)

The remaining 3 review-surplus candidates (Sasha Luccioni — age-flagged 2023 TED talk; Andrew Yang — age-flagged, lowest views; Demis Hassabis 2nd-topic — weaker re-upload sourcing) stay in `review` as the next-best promotion candidates.

**BACKLOG BACK AT THE 100 CAP: 100/100 1M+ clips found - review or raise the cap.** Available 100/100 (unchanged net), review 12 (was 14, -2 promoted), posted 2 (new this run). No Apify quota errors.

### Hooks for the 2 promoted additions

**Bernie Sanders — interviewing Claude on AI privacy (4,906,643 views)**
1. Bernie Sanders sat down with an AI. It admitted something unsettling.
2. Bernie Sanders asked Claude a question. The answer worried him.
3. Bernie Sanders interviewed an AI instead of a person. Here's why.

**Molly Crabapple — the greatest art heist in history (1,142,612 views)**
1. Molly Crabapple says artists just lived through history's biggest heist.
2. Molly Crabapple named the heist nobody is calling a crime.
3. Molly Crabapple says AI didn't borrow from artists. It stole.

### UNCONFIRMED flags
None new this run — both promoted candidates have fully confirmed official-account sourcing (Senate YouTube channel, 60 Minutes/CBS account).

## 2026-07-29 — Run #9: Apify monthly quota exhausted, no changes made

Backlog entered this run already at the 100/100 cap (unchanged since the 2026-07-28 run #8).

**STEP 1 (@theaibolt resweep):** `apify/instagram-reel-scraper` for `theaibolt` (resultsLimit 200) failed: **"Monthly usage hard limit exceeded."** Source-history could not be refreshed this cycle. Last known-good sweep remains 2026-07-28 (143/143 items, zero new since 2026-07-09).

**STEP 1b (@theaiaxon dedup):** The Apify published-reels scrape for `theaiaxon` (resultsLimit 100) failed with the same **"Monthly usage hard limit exceeded"** error. Re-probed with a minimal `resultsLimit: 5` call to rule out a parameter issue — failed identically, confirming this is an account-wide monthly cap, not an actor/input problem.

The Metricool half of STEP 1b did succeed: `getScheduledPosts` (brandId 6566296, 2026-06-29 to 2026-08-28, America/Chicago) returned only the single already-tracked Elon Musk/Dwarkesh HAL-9000 post (`PUBLISHED`, already in `theaiaxon_published_exclusions`) — no new scheduled items.

**Per protocol, because the published-reels half of the dedup check could not run, this cycle is NOT fully deduped against @theaiaxon's published library.** No pruning (STEP 2) was performed on that basis — acting on stale published-reel data risked leaving a just-posted duplicate in the pool, or worse, pruning something incorrectly. The backlog was left exactly as run #8 left it: available 100/100, review 12, posted 2.

**STEP 3/4 (discovery):** Not needed — available_count was already at the 100 cap before this run. Would have been blocked by the same quota exhaustion regardless.

**Files changed this run:** only the `last_updated` timestamp and `status`/`notes` narrative fields in `data/backlog.json` and `data/found_clips.json`, recording the quota block. No candidates added, pruned, or promoted.

**NEXT RUN:** retry the @theaiaxon published-reels scrape first, before anything else, to close this one-day dedup gap. If Apify quota is still exhausted, keep skipping pruning/discovery and keep reporting the gap explicitly rather than assuming a clean dedup.

### UNCONFIRMED flags
None new this run (no discovery performed).

## 2026-07-30 — Run #10: Apify monthly quota still exhausted, no changes made

Backlog entered this run already at the 100/100 cap (unchanged since the 2026-07-28 run #8).

**STEP 1 (@theaibolt resweep):** `apify/instagram-reel-scraper` for `theaibolt` (resultsLimit 200) failed immediately: **"Monthly usage hard limit exceeded."** Source-history could not be refreshed this cycle. Last known-good sweep remains 2026-07-28 (143/143 items, zero new since 2026-07-09).

**STEP 1b (@theaiaxon dedup):** The Apify published-reels scrape for `theaiaxon` (resultsLimit 100) failed with the same **"Monthly usage hard limit exceeded"** error. This is now the **4th consecutive day** of account-wide Apify exhaustion (2026-07-27/28 onward per run #9's history, confirmed again today).

The Metricool half of STEP 1b did succeed: `getScheduledPosts` (brandId 6566296, 2026-06-30 to 2026-08-29, America/Chicago) returned only the single already-tracked Elon Musk/Dwarkesh HAL-9000 post (`PUBLISHED`, already in `theaiaxon_published_exclusions`) — no new scheduled items.

**Per protocol, because the published-reels half of the dedup check could not run, this cycle is NOT fully deduped against @theaiaxon's published library.** No pruning (STEP 2) was performed on that basis. The backlog was left exactly as run #9 left it: available 100/100, review 12, posted 2.

**STEP 3/4 (discovery):** Not needed — available_count was already at the 100 cap before this run. Would have been blocked by the same quota exhaustion regardless.

**Files changed this run:** only the `last_updated` timestamp and `status`/`notes` narrative fields in `data/backlog.json` and `data/found_clips.json`, recording the continued quota block. No candidates added, pruned, or promoted.

**NEXT RUN:** retry the @theaiaxon published-reels scrape first, before anything else, to close the growing dedup gap. If Apify quota is still exhausted, keep skipping pruning/discovery and keep reporting the gap explicitly rather than assuming a clean dedup just because several days have passed without one.

### UNCONFIRMED flags
None new this run (no discovery performed).
