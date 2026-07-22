# IG Clips - Daily AI Clip Discovery Engine

Finds viral AI podcast/interview clips on Instagram and X every day.
Deduplicates across runs so nothing is ever surfaced twice.
Outputs a CSV report with 3 hook variations per clip.

---

## How it works

1. **Audits @brainsbyai** first - registers already-posted clips so they're never flagged
2. **Searches Instagram + X** using the full keyword framework (Tier 1–3 speakers, topics, industry disruptions, viral moments, source platforms)
3. **Qualifies each clip** - format, duration (30–90s), date (last 12 months), content pillar, spoken AI relevance
4. **Deduplicates** against `data/found_clips.json` - any URL ever found is permanently excluded from future runs
5. **Generates 3 hook options** per clip via Claude API
6. **Outputs** a dated CSV to `output/clips_YYYY-MM-DD.csv`

---

## Setup

### Local

```bash
pip install -r requirements.txt
playwright install chromium

cp .env.example .env
# Fill in your credentials in .env

cd src
python main.py
```

### GitHub Actions (automated daily)

1. Push this repo to GitHub
2. Go to **Settings → Secrets and variables → Actions** and add:
   - `INSTAGRAM_USERNAME`
   - `INSTAGRAM_PASSWORD`
   - `FIRECRAWL_API_KEY`
   - `ANTHROPIC_API_KEY`
   - `COMPOSIO_API_KEY`
   - `METRICOOL_API_KEY`
   - `APIFY_API_KEY`
3. The workflow runs daily at **8:00 AM UTC** automatically
4. Download the CSV from the **Actions → Artifacts** tab after each run

---

## Deduplication

`data/found_clips.json` is committed back to the repo after every run.
This is the single source of truth - if a URL is in this file, it will never appear again.

---

## Output format (CSV columns)

| Column | Description |
|---|---|
| clip_number | Sequential number for the run |
| platform | instagram / x |
| url | Direct link to the clip |
| views | View count at time of discovery |
| date_posted | When the clip was posted |
| speaker | Speaker name extracted |
| topic | What the speaker talks about |
| duration_sec | Clip length in seconds |
| content_pillars | Educational / Inspirational / Emotional / Controversial |
| original_source | Podcast or event name |
| full_episode_link | YouTube or Spotify link |
| interview_date | When the original interview was recorded |
| credits_handle | @handle to credit in caption |
| already_on_brainsbyai | Yes / No |
| already_on_competitor | Yes / No |
| hook_1 / hook_2 / hook_3 | Three hook variations |
| low_views_flag | ⚠️ if under 500k views |
| pillar_unverified | ⚠️ if content pillar could not be confirmed |
