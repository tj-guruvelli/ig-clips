
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
