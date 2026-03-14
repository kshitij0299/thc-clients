# Weekly Funding-Leads Automation

This document describes the automated workflow for maintaining weekly funding-leads CSVs for multiple geographies in this repo.

---

## Repo layout (current structure)

- **Top-level folders:**
  - `Indian Startups/`
  - `US Startups/`
  - `UK Startups/`
  - `Master/` – aggregated verified master CSV only (see section 6).

- **Inside each `<Geo> Startups/` folder:**
  - **Geo-specific enrichment guide:** `enrichment_instructions-<GEO>.md`  
    e.g. `enrichment_instructions-INDIA.md`, `enrichment_instructions-US.md`, `enrichment_instructions-UK.md`
  - **Geo-specific agent/rules file:** `AGENTS-<GEO>.md`
  - **Zero or more CSVs** for that geo:
    - Currently, only `Indian Startups/` has at least one CSV (e.g. `india-12_March_26.csv`).
    - `US Startups/` and `UK Startups/` have no CSVs yet.

---

## 1. DISCOVER GEO FOLDERS AND CONFIG

- From the repo root, list all top-level folders whose names end with ` Startups`.
- For each such folder, treat it as one geography (e.g. Indian, US, UK).
- Within each geo folder, locate:
  - The enrichment instructions file: `enrichment_instructions-*.md`
  - The agents/rules file: `AGENTS-*.md`
- Read both files and **strictly follow** their rules (funding year 2026, geography scope, exclusions, contact priorities, etc.).

---

## 2. CREATE THIS WEEK'S CSV PER GEO (ALWAYS NEW, 20 LEADS)

For each `<Geo> Startups/` folder:

### 2.1 Define this week's CSV filename

- Use a consistent pattern, e.g.:
  - **India:** `india-<DD>_<MonthName>_YY.csv`
  - **US:** `us-<DD>_<MonthName>_YY.csv`
  - **UK:** `uk-<DD>_<MonthName>_YY.csv`
- The exact prefix (`india`, `us`, `uk`) can be derived from the folder name or instructions, but ensure:
  - It is **stable over time** per geo.
  - The date reflects **this week's run** (e.g. `19_March_26`).

### 2.2 Determine the header

- **If there is an existing CSV** in that geo folder: use its header row exactly.
- **If there is no existing CSV** (e.g. initial runs for US/UK):
  - Construct the header from `enrichment_instructions-<GEO>.md`.
  - At least these columns:
    - Startup Name
    - Website
    - Industry
    - Funding Stage
    - Funding Amount (Text)
    - Funding Date (YYYY-MM)
    - Funding Source (URL)
    - Funded By
    - Founder Name
    - Founder Role
    - Founder LinkedIn URL
    - Founder Email
    - Company Size (Approx)
    - Likely Hiring Roles
    - Hiring Signal
    - Outreach Priority

### 2.3 Create a fresh CSV file for this week

- Create the new CSV in the `<Geo> Startups/` folder with the **header row only** to start.
- **DO NOT** copy all previous rows; this file should contain only **NEW** startups found during this run.

---

## 3. RESEARCH AND ADD ~20 NEW LEADS PER GEO (FUNDING IN 2026)

For each geo, aim to add around **20 *new* startups** that:

- Match that geo's scope (e.g. Indian startups for India, UK startups for UK, etc.).
- Have funding rounds **clearly announced in calendar year 2026**.
- Are **product-led startups** (not IT services agencies, consultancies, or large enterprises).

### 3.1 Dedup across previous runs

- Collect all **existing CSVs** in that `<Geo> Startups/` folder (including older weeks).
- Maintain a set of **previously seen startups**, using:
  - **Normalized Startup Name** (lowercase, trimmed; optionally strip generic suffixes like Labs/Technologies/Solutions when clearly the same).
  - And/or **Website domain** when available.
- When considering a candidate startup, **skip it** if it already appears in any older CSV for that geo.

### 3.2 Use Browserbase + open web to discover candidates

- Use **Browserbase** (Stagehand or anything else) to:
  - Search news/press, funding roundups, VC portfolio pages, etc., following the search patterns in `enrichment_instructions-<GEO>.md` (e.g. for India: YourStory, Inc42, Entrackr, BW Disrupt, Economic Times, etc.; for US/UK: analogous sources defined in those instructions).
  - Filter for funding articles where:
    - The company is in the **correct geography or origin** for that geo.
    - The funding announcement is **clearly in 2026**.
- For each candidate article:
  - Confirm 2026 funding and correct geography.
  - Skip if the company is already in the dedup set.
- **Use built-in internet/search tools** in case Browserbase does not work.

### 3.3 For each accepted startup, populate a row

Extract and fill at least:

- Startup Name
- Website (official domain, verified through the article and/or company site)
- Industry (using the **controlled vocabulary** from the instructions: Spacetech, Fintech, Healthtech, Enterprise SaaS, Deeptech, D2C, Proptech, Logistics, Defence Tech, etc.)
- Funding Stage (Seed, Series A, etc.)
- Funding Amount (Text) (copy the amount string as written, e.g. `$6.3M`, `₹70 Cr`)
- Funding Date (YYYY-MM) (derive from the article date or explicit round date)
- Funding Source (URL) (the article link)
- Funded By (lead and notable investors; semi-colon or comma separated as per instructions)

---

## 4. ENRICH CONTACTS (FOUNDER LINKEDIN + EMAIL) FOR EACH NEW ROW

For each new startup row added in this run:

### 4.1 Identify at least one decision-maker

- Use Browserbase to:
  - Open the company website; check About / Team / Leadership / Founders pages.
  - Run name + company searches on Google and news/press profiles.
- Follow **AGENTS-<GEO>.md** priority order:
  1. Founder / Co-founder / CEO  
  2. CTO / CPO / COO / Co-founder (technical or product)  
  3. Head/VP Engineering or Product  
  4. Head/VP Talent/People/HR  

### 4.2 For the chosen contact

- **Find a public LinkedIn profile URL** that clearly matches the person and startup:
  - Must be a `linkedin.com/in/...` URL.
  - Confirm via job title, company name, or description in the profile snippet/page.
- **Look for a public email:**
  - On the company's Contact/Team/Press/Careers pages.
  - On the person's personal site if linked.
  - On clearly public press releases or reputable directories.

### 4.3 Data quality rules

- **ONLY** record emails that are plainly visible on public pages.
- **NEVER** guess or pattern-generate emails (e.g. `first.last@company.com`).
- If no confident LinkedIn match is found, leave **Founder LinkedIn URL** blank.
- If no public email is found, leave **Founder Email** blank.
- Prefer **high-confidence fewer contacts** to many low-quality or wrong contacts.

### 4.4 Fill the row

Set:

- Founder Name  
- Founder Role  
- Founder LinkedIn URL (if found)  
- Founder Email (if found)  
- Company Size (Approx) from LinkedIn/company info, bucketed as: 1–10, 11–50, 51–200, 201–500, 500+  
- Likely Hiring Roles, Hiring Signal, Outreach Priority (following `enrichment_instructions-<GEO>.md`).

**Stop** when you have ~20 fully processed startups for that geo **OR** you run out of solid 2026 candidates.

---

## 5. WEEKLY VERIFICATION PASS

After building all new CSVs:

### 5.1 For each newly created CSV

- Verify each row:
  - **Startup Name** and **Funding Source (URL)** are non-empty.
  - **Funding Date (YYYY-MM)** contains `2026`.
  - **Industry** uses the allowed label set from the instructions.
  - No obviously placeholder values (e.g. `N/A`, `test`, `foo`) in key fields.
- Do **not** silently keep startups that violate the 2026 or geography rules; instead, **drop them** from the CSV and note this in the summary.

### 5.2 Compute stats per new CSV

- Total number of rows (startups).
- Count with non-empty **Founder LinkedIn URL**.
- Count with non-empty **Founder Email**.

### 5.3 Produce a markdown summary in the run output

For each geo (Indian/US/UK) processed:

- New CSV filename.
- Total startups; # with LinkedIn; # with email.
- Any notable issues (e.g. couldn't find enough valid 2026 startups to reach 20; ambiguous founder identity; no public emails).

---

## 6. BUILD MASTER CSV (END OF EVERY RUN)

After the verification pass (section 5), **always** run the Master build so the combined verified list is updated.

### 6.1 What it does

- **Builds** `Master/master_startups.csv` from **all** `*.csv` files under the repo (excluding the `Master/` folder).
- **Verified only:** includes only rows that have at least **Founder LinkedIn URL** or **Founder Email** (non-empty).
- **Deduplicates** by **Startup Name** (case-insensitive); adds a **Country** column from the top-level folder name (e.g. Indian Startups, UK Startups, US Startups).

### 6.2 How to run it

From the **repo root**:

```bash
python3 "Master/build_master_csv.py"
```

Or use the pipeline script (same effect):

```bash
python3 "Master/run_master_pipeline.py"
```

### 6.3 When to run it

- Run **at the end of every automation run**, after verification (section 5).
- Then proceed to git/PR if applicable (section 7).

---

## 7. GIT / PR BEHAVIOR

- **Stage only** the new CSVs created in this run.
- **If** the "Open Pull Request" tool is enabled:
  - Open a PR on the selected branch (e.g. `main`) titled:  
    **Weekly leads enrichment – &lt;YYYY-MM-DD&gt;**
  - Include the summary from step 5.3 in the PR body.

---

## 8. GENERAL QUALITY RULES

- Always obey each geo's `enrichment_instructions-<GEO>.md` and `AGENTS-<GEO>.md`.
- Prefer **accuracy over volume**: do not fabricate data to hit exactly 20 entries; “~20 high-quality leads” is the goal, not a hard quota.
- **Never** invent founders, LinkedIn URLs, or emails; leave fields blank when not confidently known.
