
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
