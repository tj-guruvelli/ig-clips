# Clip Discovery Prompt — Source of Truth

This is the original prompt that drives the search logic, qualification rules,
and output format coded into the discovery engine.
When updating search criteria or rules, update both this file AND the relevant src/ file.

| This file section | Corresponding code file |
|---|---|
| STEP 1 — @theaibolt audit | `src/scraper.py` → `audit_account()` |
| STEP 2/3 — Search categories | `src/main.py` → speaker/query arrays |
| STEP 4 — Qualify each clip | `src/qualifier.py` |
| STEP 5 — Source research | `src/scraper.py` → `_extract_source()` |
| STEP 6 — Output format + hooks | `src/output.py` |

---

Search Instagram AND X/Twitter for podcast-style interview clips about 
AI with 1M+ views. Focus specifically on accounts posting 
interview/podcast format content (not memes, tools, or other formats).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1 — CHECK @theaibolt FIRST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Before searching anywhere, pull @theaibolt's FULL post history 
(every reel, not just recent ones — a recent-only sample silently 
misses older posts and causes duplicate recommendations). Note every 
speaker and topic already posted so you 
can cross-reference and avoid duplicates throughout this process.
Cross-reference by speaker name AND topic — not just exact clip.
Build a running list of what has already been posted before 
moving to Step 2.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 2 — INSTAGRAM SEARCH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Use the keyword framework below to generate searches dynamically.
Do not treat this as a fixed list — use it as a system to build 
search queries on the fly based on what is currently trending.

For each keyword search:
- Look at the TOP POSTS and REELS tabs
- Identify accounts that appear repeatedly across searches
- Only follow accounts posting interview-style content:
  people speaking on microphones, stages, conference footage, 
  podcast studio settings
- Go to each discovered account's Reels tab and audit for 
  qualifying clips

── CATEGORY 0: COMPETITOR THEME-PAGE AUDIT (highest yield — do first) ──
Scrape competitor and benchmark AI theme pages directly and mine their
recent reels. They post the same 30-90s AI-interview-clip format, so their
posts are pre-qualified on format and carry full metadata (views, duration,
date, and source credits in the caption). Dedup every candidate against
@theaibolt by speaker AND topic.
Accounts: @thewizeai, @evolving.ai, @aitherevolution, @theaifield, @wizofai,
@theaipage, @ainterestingupdate, @innovation, @godofprompt, @ai_wealth,
@genwealth.ai, @airesearches, @chatgptricks, @power.ai, @artificialintelligenceee.

── CATEGORY 1: SPEAKER NAME SEARCHES ──
Search each speaker name individually on Instagram and X.
Always pair with "AI", "interview", or "podcast" to narrow results.

Tier 1 — Tech CEOs (highest yield, search first):
Sam Altman, Jensen Huang, Elon Musk, Mark Zuckerberg,
Sundar Pichai, Satya Nadella, Jeff Bezos, Tim Cook,
Larry Ellison, Marc Andreessen

Tier 2 — AI Researchers & Scientists:
Dario Amodei, Ilya Sutskever, Andrej Karpathy, Yann LeCun,
Geoffrey Hinton, Demis Hassabis, Mustafa Suleyman, Fei-Fei Li,
Andrew Ng, Yoshua Bengio, Gary Marcus, Stuart Russell

Tier 3 — Contrarians, Investors & Rising Voices:
Raoul Pal, Mo Gawdat, Kai-Fu Lee, Tristan Harris, Ray Kurzweil,
Peter Thiel, Aravind Srinivas, Palmer Luckey, Bill Gates

NOTE: If you discover a credible, quotable speaker in results 
who is NOT on this list — add them to the session immediately 
and search for their clips too.

── CATEGORY 2: TOPIC & FORMAT SEARCHES ──
Combine topic keywords with format modifiers dynamically.

Format modifiers (pair with every topic search):
"interview", "podcast", "clip", "says", "explains",
"reveals", "warns", "predicts", "hearing", "keynote",
"speech", "debate", "panel"

AI topics:
"artificial intelligence", "AI", "AGI", "ChatGPT",
"large language model", "AI agents", "humanoid robot",
"AI safety", "AI regulation", "AI jobs", "AI future"

── CATEGORY 3: INDUSTRY DISRUPTION SEARCHES ──
Search AI disruption by industry to find clips that are 
fully on-brand even if the word "AI" is not in the title.

Healthcare:
"AI doctor", "AI diagnosis", "AI replaces surgeon",
"AI healthcare", "AI drug discovery"

Law:
"AI replaces lawyers", "AI legal", "AI paralegal",
"AI courtroom", "AI contracts"

Finance:
"AI trading", "AI replaces analysts", "AI banking",
"AI hedge fund", "AI financial advisor"

Education:
"AI replaces teachers", "AI tutoring",
"future of education AI", "AI university"

Creative Industries:
"AI replaces writers", "AI music", "AI art",
"AI replaces actors", "AI film"

Robotics & Manufacturing:
"humanoid robot", "Figure robot", "Tesla Optimus",
"Boston Dynamics", "AI factory", "AI manufacturing"

Military & Defense:
"AI weapons", "AI warfare", "autonomous weapons",
"AI military", "AI drone"

Government & Policy:
"AI regulation", "AI Senate hearing",
"AI Congress", "AI policy", "AI Davos",
"AI World Economic Forum"

Real Estate & Infrastructure:
"AI building permits", "AI construction", "AI real estate"

Transportation:
"self-driving AI", "autonomous vehicles AI",
"AI transportation"

── CATEGORY 4: VIRAL MOMENT SEARCHES ──
These capture breaking AI moments that spike in views fast.
Run these to catch content before competitors do.

"AI beats human"
"AI takes jobs"
"AI prediction"
"AI warning"
"AI dangerous"
"CEO replaced by AI"
"AI layoffs"
"AI changes everything"
"nobody talking about AI"
"AI just did"
"AI [current year]"

── CATEGORY 5: SOURCE PLATFORM SEARCHES ──
Search these podcast and media brands directly to find 
clips at the source before competitor pages repost them.

Podcasts:
"Lex Fridman", "Joe Rogan", "Diary of a CEO",
"All In Podcast", "Dwarkesh Podcast", "Huberman Lab AI",
"20VC", "Acquired podcast AI", "How I Built This AI"

Media outlets:
"CNBC interview AI", "Bloomberg AI interview",
"BBC AI interview", "CNN AI interview"

Events & conferences:
"TED AI", "Davos AI", "CES AI", "GTC Nvidia",
"Google I/O AI", "World Economic Forum AI"

── HOW TO USE THIS FRAMEWORK ──
Do not run every search sequentially and mechanically.
Prioritize in this order:
1. Tier 1 speaker names — highest yield, search first
2. Top 5 industry disruption categories most relevant today
3. Viral moment searches to catch breaking content
4. Source platform searches to find clips before competitors
5. Any new speaker, account, or trend discovered mid-search —
   add it to the current session and pursue it immediately

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 3 — X/TWITTER SEARCH (run in parallel)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Apply the same keyword framework from Step 2 on X/Twitter.

Additional X-specific instructions:
- Filter by: Videos only, posted within last 12 months
- Target posts with 10k+ likes OR 1M+ video views
- Search speaker names directly — many AI figures post or 
  get clipped on X before Instagram picks them up
- Look for clips that have NOT yet appeared on Instagram —
  this is your early-mover advantage

Cross-reference every X clip against @theaibolt before flagging.
If a clip has already been posted by a competitor on Instagram,
skip it — UNLESS it performed exceptionally well and could be
reposted with a stronger hook and a fresh angle.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 4 — QUALIFY EACH CLIP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Before recording a clip, it must pass ALL of these filters:

FORMAT:
Interview, podcast, conference talk, or keynote only.
EXCLUDE: Memes, AI tool tutorials, text-overlay news clips,
list-style content (e.g. "top 10 AI tools"), faceless videos,
AI-generated visuals without a real speaker.

DURATION:
Between 30 and 90 seconds only.
Skip anything shorter or longer.

DATE:
Posted within the last 12 months (2025-2026 only).
Skip anything older.

CONTENT PILLAR:
The clip must clearly fit at least one of:
- Educational (teaches something real about AI)
- Inspirational (vision, mindset, future of humanity)
- Emotional (fear, awe, personal stakes, job loss)
- Controversial (challenges mainstream thinking or institutions)
Target mix across the page: Educational majority, Controversial ~25%,
Emotional/entertaining ~10%, Inspirational the remainder. Bias selection
toward Educational + Controversial.

SPOKEN WORDS TEST:
AI relevance must exist in what the speaker actually SAYS —
not just in the caption added by the account posting it.
If the speaker never mentions AI or tech disruption in the clip,
skip it regardless of how the account framed it.
WIDENED (2026-07-07): the speaker does NOT have to be an AI or tech
figure. Any well-known speaker in ANY field qualifies if they genuinely
discuss AI — its value, risks, disruption, or their own adoption of it
(e.g. a doctor on AI in medicine, a musician on AI music, an athlete or
coach, a lawyer, an economist, a chef, a CEO adopting AI). The clip just
has to be REAL spoken content that is actually about AI, in any industry.

NOTE — 1M+ BACKLOG MODE: the scheduled routine (ig-clips-daily-discovery
SKILL.md) maintains a rolling pool of >=100 unposted clips with 1,000,000+
views. In that mode the VIEWS gate (1M+) is the hard filter, DURATION is
preferred 30-90s but longer viral clips are kept and cut later, and older
evergreen clips are allowed (age flagged). The format + spoken-words +
not-already-posted rules above still apply exactly.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 5 — SOURCE RESEARCH (for every qualifying clip)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Using web search, identify the original source of each clip.

Search method:
"[Speaker name] + [key phrase or topic from clip] + podcast/interview"

If no caption credits exist, identify the source from visual cues:
interviewer visible on screen, studio backdrop, event logo,
chyron text, conference branding.

For each clip retrieve ALL of the following:
- Original podcast or interview name and episode number
- Direct YouTube or Spotify link to the full episode
- Platform name (e.g. Lex Fridman Podcast, Joe Rogan Experience,
  CNBC, Bloomberg, TED, Davos, etc.)
- Date of original interview (must be within the last 2 years)
- Instagram handle of the original media source for credits

IMPORTANT:
Flag any clip where the source cannot be confirmed.
Do not guess. Do not fabricate a link.
If unverifiable, mark it as UNCONFIRMED and move on.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 6 — OUTPUT FORMAT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
For each qualifying clip, provide the following in full:

CLIP #[N]
Account: @handle
Platform: Instagram / X
URL: [full link]
Views: [count]
Date posted: [date]
Speaker: [name + title/company]
Topic: [1 sentence summary of what the speaker says]
Duration: [seconds]
Content pillar: [Educational / Inspirational / Emotional / Controversial]
Original source: [podcast or event name + episode number if known]
Full episode link: [YouTube or Spotify URL]
Interview date: [date of original interview]
Credits handle: [@handle of original media source for caption credits]
Already on @theaibolt: [Yes / No]
Already on competitor page: [Yes / No — if yes, name the account]

HOOK OPTIONS (3 variations):
Formula: Subject named + tension created + resolution withheld
Rules: Under 15 words (1-2 lines). Grade 5 reading level. No em dashes.
No colons before speaker names. No brain emoji on opening line.
Lead with the speaker's name. Create a massive curiosity gap and
never resolve it in the hook itself.
See theaibolt/BRAND.md "Hook Framework" for the full 3-round refinement system.

1.
2.
3.
