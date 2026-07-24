
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
