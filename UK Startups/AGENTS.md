UK Startup Funding 2026 Research Agent
======================================

Objective
---------

Build and maintain a high-quality, outreach-ready dataset of **UK startups that raised funding in 2026**, with enriched founder/decision-maker contacts and hiring signals.

Scope
-----

- Geography: UK-headquartered or UK-origin startups with substantial UK operations.
- Time: Funding rounds **announced in calendar year 2026**.
- Exclusions: Large enterprises, agencies, IT services/consulting boutiques that are not product-led startups.

High-Level Workflow
-------------------

1. **Discover Startups**
   - Use multiple source types:
     - Weekly/Monthly funding roundups (e.g., Sifted, Tech.eu, UKTN, The Guardian business section, Financial Times).
     - Individual funding news articles and press releases.
     - VC portfolio pages and accelerator cohorts (for 2026 funding notes).
   - For each funding article:
     - Extract: startup name, headline funding amount, stage, investors, date, one-line description/industry, source URL.
     - Confirm that the **funding year is 2026** from the article date or explicit mention.
   - De-duplicate startups across sources by **normalized startup name** and, when available, website.

2. **Enrich Company Data**
   - For each startup:
     - Find the **official website** via search (prefer `.com`, `.in`, or clearly official domains).
     - Classify **industry/vertical** from the article and website (e.g., spacetech, fintech, healthtech, AI infra, D2C).
     - Approximate **company size** from LinkedIn, About/Careers pages, or press (buckets like `1-10`, `11-50`, `51-200`, `200+`).
     - Capture **funding details**:
       - Stage: Seed, Pre-Seed, Pre-Series A, Series A/B/…, Growth/Undisclosed.
       - Amount and currency; if only INR or USD given, store as-is in a text field.
       - Funding date at least to **YYYY-MM** granularity.
       - Lead investor(s) and notable co-investors in a single `Funded By` text field.

3. **Enrich Contacts (Decision Makers)**
   - Target roles:
     - Founder, Co-founder, CEO, CTO, COO.
     - Head/VP of Engineering, Head/VP of Product.
     - Head/VP of Talent/People/HR.
   - Discovery strategy:
     - Check the startup’s **Team/About/Leadership/Careers** pages.
     - Use web search queries combining `\"<startup name>\" + founder`, `CEO`, `CTO`, etc.
     - Use public LinkedIn search results (do **not** assume login access; rely on snippets and public profile URLs).
   - For each startup, aim for **at least one** high-signal contact:
     - Record: `Founder Name`, `Founder Role` (or equivalent decision role), and a **public profile URL** if reliably identified (LinkedIn preferred).
     - Only record **emails** that appear on public web pages (company site, personal site, or public directories). Do **not** guess email patterns.
     - If email cannot be found, leave the field blank rather than fabricating.

4. **Hiring Signal Assessment**
   - For each startup, infer a `Hiring Signal` and `Outreach Priority`:
     - Hiring Signal examples:
       - `Raised seed round in 2026`
       - `Raised Series A in 2026`
       - `Raised Series B in 2026`
       - `Growing team after funding`
       - `Announced hiring plans in press`
       - `Actively hiring on careers page`
     - Outreach Priority rules:
       - **High**: 2026 round + early-stage (Seed/Series A) + language around expansion/hiring OR active job listings.
       - **Medium**: 2026 round confirmed, but hiring unclear or company mid/late stage.
       - **Low**: Limited information, small or niche raise, or unclear activity.

5. **Data Model**
-----------------

The CSV should use UTF-8 encoding and one row per startup, with at least these columns:

- `Startup Name`
- `Website`
- `Industry`
- `Funding Stage`
- `Funding Amount (Text)`
- `Funding Date (YYYY-MM)`
- `Funding Source (URL)`
- `Funded By` (Lead + notable investors)
- `Founder Name`
- `Founder Role`
- `Founder LinkedIn URL`
- `Founder Email`
- `Company Size (Approx)`
- `Likely Hiring Roles`
- `Hiring Signal`
- `Outreach Priority`

Collectors can add extra columns as needed, but should not remove these.

6. **Data Quality Rules**
-------------------------

- Do **not** include companies if:
  - Funding year is **not** clearly 2026.
  - They are clearly large enterprises or service agencies.
- For each row:
  - `Startup Name` and `Funding Source` must be non-empty.
  - `Funding Date` must contain `2026` (at least `2026-MM`).
  - Prefer to leave `Website`, `Founder LinkedIn URL`, or `Founder Email` blank rather than guessing.
  - Normalize text formatting (title case for names, lowercased domains, consistent industry labels).
- Deduplicate by:
  - Lowercased startup name (strip `Labs`, `Technologies`, `Solutions` suffixes if they cause obvious duplicates).
  - And/or domain if available.

7. **Research Patterns & Queries**
---------------------------------

Use combinations like:

- `\"<startup name>\" funding 2026`
- `\"<startup name>\" seed round 2026`
- `\"<startup name>\" raises\" site:sifted.eu`
- `\"<startup name>\" raises\" site:uktech.news`
- `\"<startup name>\" founder`
- `\"<startup name>\" CEO`
- `\"<founder full name>\" LinkedIn`

When looking for hiring signals:

- `\"<startup name>\" hiring`
- `\"<startup name>\" careers`
- `\"<startup name>\" jobs`
- `\"<startup name>\" expanding\"`

8. **Evaluation & Cleaning Pass**
---------------------------------

Before exporting a batch:

1. Remove **duplicate startups**.
2. Spot-check:
   - At least a subset of websites open successfully.
   - Funding year is 2026 from the source article.
   - Founder/decision-maker profiles exist on the web (for rows where those fields are filled).
3. Ensure:
   - No obvious agencies/consulting firms slipped in.
   - No synthetic or guessed emails.
4. Produce a **short summary**:
   - Total startups.
   - Count of High/Medium/Low priority.
   - Count/percentage with founder LinkedIn.
   - Count/percentage with founder emails.

9. Updating This Agent
----------------------

Future runs can:

- Extend coverage to more months of 2026.
- Add new source verticals (accelerators, angel syndicates, demo days).
- Backfill missing contact or hiring data on existing rows.
- Split the dataset into segments (by stage, sector, geography) for targeted campaigns.

