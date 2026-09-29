---
name: daily-cause-list
description: Produce an image-first daily court cause list and hearing schedule from supplied CSV, pasted records, spreadsheet, or screenshots.
---
# Daily Cause List / Hearing Schedule

## Triggers
Use for "cause list", "course list" (speech-to-text variant), "daily cause list", "hearing schedule", "make court list", "generate cause-list image", and equivalent requests. This is a standalone schedule skill, NOT the petition or legislation-writing skill. Do not impose petition top spacing. Do not load unrelated skills.

## Inputs and source of truth
Accept CSV header such as:
`CNR Number,Case Number,Petitioner,Respondent,Judge Name,Court Name,Stage,Current Hearing Date,Previous Hearing Date,Next Hearing Date,Case Type,Notes,Tags`.
Also accept an uploaded table, structured text or screenshots. The actual supplied rows override the sample. Read all rows, including long party names; never populate a new cause list with old example case data.
- Current Hearing Date is the schedule date. Confirm whether all rows have the same date; if mixed, split by date or explicitly label the range.
- Convert source dates (including M/D/YYYY) to DD/MM/YYYY without swapping month and day. Preserve each distinct previous/next date. Blank next date -> en dash or hyphen, meaning not provided, NOT an inferred future date.
- Keep case number, CNR, petitioner, respondent, judge, court, stage and classification exactly as supplied. Do not silently correct spelling (including unusual stage labels), invent a judge, or infer a hearing date.
- Derive Total Listed and Civil/Criminal summary from actual rows. Classifications containing Criminal (Complaint), Criminal (POCSO/JJ Act), etc count under Criminal; Civil counts under Civil. If other categories occur, state them rather than misclassify.
- Notes and tags inform context but are not automatically table columns. Preserve source record separately when useful.

## Saved visual prompt and layout
Create a clean, polished, HIGH-RESOLUTION landscape judicial schedule IMAGE matching the user-approved example's *style*: white or very pale cool background; thin dark navy rounded outer border; classic bold serif headings; navy/black text; subtle pale-blue header cells/optional alternating pale row tints; crisp fine table grid; professional and restrained spacing. Never copy the example's parties or dates.

Centered top lines:
1. IN THE COURT OF THE DISTRICT & SESSIONS JUDGE / CJM, JAMSHEDPUR [only when this is the supplied court context; otherwise adapt accurately]
2. OFFICIAL DAILY CAUSE LIST & HEARING SCHEDULE [treat this as the requested visual title, not proof of court issuance]
3. Daily Cause List for DD/MM/YYYY
4. Total Listed: N • Civil: C • Criminal: K • Mode: Full Cause List • Standard Format: DD/MM/YYYY

After a horizontal separator use a nearly full-width, readable 9-column table in this precise order:
`# | Case No. & CNR | Parties | Court & Presiding Judge | Stage | Type | Hearing Date | Previous Date | Next Hearing Date`.
- In case cell: bold case number above smaller CNR.
- In parties cell: petitioner in bold first line, then 'vs' and respondent, wrap naturally, never truncate a name.
- In court cell: bold court name above smaller judge name.
- Stages/type fit with legible wrapping. Dates centered. All records numbered in original supplied order, unless user requests another sort.
- Use enough vertical space for long names; never overlap, omit, merge or duplicate rows. If 11+ records cannot fit legibly in one image, create a consistent multipage/image series with repeated table headings, page number, and per-page record continuity, without shrinking text to illegibility.
- Footer rule. Left: 'Prepared in accordance with Judicial Cause List Standards' and 'All dates formatted as DD/MM/YYYY • Total Active Cases in this docket: N'. Right: 'Signature of Bench Reader / Clerk' and 'COURT OF DISTRICT & SESSIONS JUDICIARY' as visual placeholders ONLY if user requests the example's footer. Leave signature blank. Where this is a privately prepared list, do not claim verification, signature, court issuance or official certification. If needed add 'User-prepared schedule; verify against official court listing.'

## Production: accuracy before generative styling
Prefer deterministic HTML/CSS -> PNG (browser screenshot or equivalent) for long text-heavy tables so names, dates and CNRs are exact. Image generation can be used for the visual style or when expressly requested, but proofread against structured data because image models may alter text. If generating directly with an image model, supply every row in the prompt and compare the resulting image to the source, then correct any discrepancy. Also offer PDF if requested; image (PNG) is the default for this skill. Preserve editable HTML/structured data where possible.

## Final checks
Count all rows; verify every CNR and case number, party spelling, date, court and stage, summary totals, table readability and footer. Never invent missing entries. Do not mistake the sample screenshot's one example case for current data. This skill formats a supplied schedule; it does not establish that listed hearings are live or officially verified.
