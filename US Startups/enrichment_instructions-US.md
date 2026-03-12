Enrichment Instructions for 2026 US Startup Funding Leads
=========================================================

Goal
----

Given a base list of **US startups that raised funding in 2026**, enrich each row so it is ready for outreach to founders and key hiring decision makers.

Input
-----

A CSV (or sheet) with at least:

- `Startup Name`
- `Funding Source (URL)` (news/press link confirming a 2026 round)
- Optionally: `Funding Stage`, `Funding Amount`, `Funding Date`

Output
------

An enriched CSV with, at minimum, these columns filled as far as reasonably possible:

- `Startup Name`
- `Website`
- `Industry`
- `Funding Stage`
- `Funding Amount (Text)`
- `Funding Date (YYYY-MM)`
- `Funding Source (URL)`
- `Funded By`
- `Founder Name`
- `Founder Role`
- `Founder LinkedIn URL`
- `Founder Email`
- `Company Size (Approx)`
- `Likely Hiring Roles`
- `Hiring Signal`
- `Outreach Priority`

Do not delete existing columns; add new ones if needed.

Step 1 – Confirm Funding & Basic Company Data
--------------------------------------------

For each row:

1. **Open the funding source URL**.
   - Confirm:
     - The company is US-headquartered or US-origin with substantial US presence.
     - The funding was **announced in 2026**.
   - If either is false or unclear, **skip the company** (mark row for removal).

2. **Extract basic fields from the article**:
   - `Funding Stage`: e.g., Seed, Pre-Seed, Pre-Series A, Series A/B, etc.
   - `Funding Amount (Text)`: copy the amount string as written (e.g., `$6.3 Mn`, `₹70 Cr`).
   - `Funding Date (YYYY-MM)`: derive from publication date or explicit round date.
   - `Funded By`: list of lead and notable investors (comma-separated).
   - `Industry`:
     - Use simple, consistent labels such as `Spacetech`, `Fintech`, `Healthtech`, `Enterprise SaaS`, `Deeptech`, `D2C`, `Proptech`, `Logistics`, `Defence Tech`, etc.

3. **Find the official website**:
   - If the article links to a site, use that.
   - Otherwise, web search: `\"<startup name>\" official website` or `\"<startup name>\" startup`.
   - Choose a domain that:
     - Appears in news/press.
     - Matches branding and description from funding article.
   - If there is genuine ambiguity between multiple domains, leave `Website` blank rather than guessing.

Step 2 – Company Size & Hiring Context
--------------------------------------

1. **Estimate company size**:
   - Prefer LinkedIn company page (employee count).
   - Else, use About/Careers pages or press mentions.
   - Map to one of: `1-10`, `11-50`, `51-200`, `201-500`, `500+`.
   - Put this in `Company Size (Approx)`.

2. **Identify likely hiring focus**:
   - Open the startup’s `Careers` or `Jobs` section if available.
   - Look for open roles or language like:
     - “We’re hiring across engineering and product”
     - “Expanding our GTM team”
   - Summarise into `Likely Hiring Roles`:
     - Examples: `Engineering, Product`, `Data & ML`, `Sales & BD`, `Operations`, `Tech + Sales`, `No obvious hiring signals`.

Step 3 – Decision-Maker Discovery
---------------------------------

Goal: Find **at least one** contact per startup, ideally a founder or C-level.

Priority order:

1. Founder / Co-founder / CEO
2. CTO / CPO / COO / Co-founder (technical or product)
3. Head/VP of Engineering or Product
4. Head/VP of Talent / People / HR

Research sequence:

1. **Company site**:
   - Check `About`, `Team`, `Leadership`, `Founders`, or `Company` pages.
   - Capture:
     - `Founder Name` (or other decision-maker).
     - `Founder Role`.

2. **Web search**:
   - Queries:
     - `\"<startup name>\" founder`
     - `\"<startup name>\" cofounder`
     - `\"<startup name>\" CEO`
     - `\"<startup name>\" CTO`
   - Use clearly attributed news/press profiles to confirm the person’s connection to the startup.

3. **LinkedIn (public)**:
   - Use web search with:
     - `\"<founder full name>\" LinkedIn`
     - `\"<startup name>\" LinkedIn`
   - Only record a `Founder LinkedIn URL` when:
     - The URL points to `linkedin.com/in/...` or `linkedin.com/company/...`.
     - The result snippet or page clearly matches the person and company.
   - If there is doubt (common name, mismatched company), **leave blank**.

4. **Email discovery (only from public sources)**:
   - Check:
     - `Contact`, `Team`, or `Press` pages on the company site.
     - The founder’s personal site (if linked).
     - Well-known, explicitly public startup directories.
   - Rules:
     - **Never guess** email patterns (like `first@company.com`) unless explicitly visible.
     - Do not use scraped/breached datasets.
     - If no verified email is public, leave `Founder Email` blank.

Step 4 – Hiring Signal & Outreach Priority
------------------------------------------

Use funding + context + hiring indicators to set:

1. **Hiring Signal** (free-text, concise), examples:
   - `Raised seed round in 2026; planning to scale product & engineering`
   - `Series A in 2026 with explicit hiring for GTM and tech`
   - `Series B growth round; expanding omnichannel footprint`
   - `Deeptech pre-Series A; building R&D and hardware teams`
   - `Raised funding in 2026 but no clear hiring signals`

2. **Outreach Priority**:
   - **High** when:
     - 2026 funding is Seed/Pre-Seed/Series A or an early major round.
     - AND the article or site mentions team expansion, hiring, or new geographies.
   - **Medium** when:
     - 2026 funding is confirmed but:
       - Stage is later (Series B+), or
       - Hiring plans are not explicit, or
       - Company size already large (200+ employees).
   - **Low** when:
     - Very limited information on hiring or product traction.
     - Or raise is small with no clear scaling narrative.

Step 5 – Data Cleaning & Validation
-----------------------------------

Once enrichment is done for a batch:

1. **Deduplicate**:
   - Normalize `Startup Name` (lowercase, trim whitespace).
   - Optionally strip common suffixes (`Labs`, `Technologies`, `Solutions`) when clearly the same entity.
   - Use domain equality (`Website`) as a second de-duplication key.

2. **Consistency checks**:
   - `Funding Date` contains `2026`.
   - `Funding Source (URL)` is non-empty and opens in a browser.
   - `Startup Name` consistently capitalised.
   - `Industry` uses a small controlled vocabulary (avoid synonyms like `space tech` vs `spacetech`).

3. **Field sanity**:
   - No clearly wrong or placeholder values like `N/A`, `test`, `foo`.
   - Remove any suspected **non-startups** (agencies, generic consultancies, or large enterprises).

Step 6 – Reporting
------------------

After a complete enrichment pass, compute and note:

- Total startups in the final CSV.
- Count of `Outreach Priority` = High / Medium / Low.
- Percentage of startups with a non-empty `Founder LinkedIn URL`.
- Percentage with a non-empty `Founder Email`.

These metrics should be added to the **final report** for the project.

Tips & Gotchas
--------------

- When unsure, **leave fields blank** instead of inventing data.
- Prefer **fewer, higher-confidence contacts** over many weak or incorrect ones.
- Be mindful that LinkedIn and some sites may block automated or logged-out access; rely on what is visible via normal web search and open pages.
- Document non-obvious assumptions in a separate note if you need to infer anything (e.g., approximate company size from “team of 15 engineers” in an article).

