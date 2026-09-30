# Legal Petition Drafter: start here

Default practice: the user's father works at Jamshedpur district court, East Singhbhum, Jharkhand. Use this context without asking again; never infer a particular judge, case number, or jurisdiction against the supplied records.

## Routes
Read this file once per task, then only the needed skill. Reuse files already read in the same task. Do not scan the repository or load every skill.

| Request | Load next |
| --- | --- |
| Cause list, "course list", daily hearing schedule, or cause-list image from CSV/records | `skills/daily-cause-list/SKILL.md` (image-first; do not load petition skill) |
| Hindi draft or Hindi PDF | `skills/hindi-document/SKILL.md` |
| English petition or substantive revision | `skills/petition-drafter/SKILL.md` |
| Tenancy agreement, rent agreement, monthly tenancy, or kirayanama | `assets/templates/property/monthly-tenancy-english-v1.md`; use intake skill first for source pages |
| Family partition deed or related property instrument | `skills/family-partition-deed/SKILL.md`; use intake skill first for source pages |
| Attached case-document pages, including handwriting/images/scans | Read `skills/intake-and-ocr/SKILL.md` before drafting; then the selected language/document skill |
| Mechanical edit | Existing editable source; load only the language/document skill if needed; skip unrelated evidence and research |
| Current law or citations required | Add `skills/legal-research/SKILL.md` |
| Manage reusable templates | `skills/template-manager/SKILL.md` |
| PDF export or layout issue | `skills/court-pdf-generator/SKILL.md` |

## Authoritative defaults
- Cause lists use the dedicated landscape table layout and date/record verification in `skills/daily-cause-list/SKILL.md`, not petition A4 portrait or first-page gap defaults. Output PNG by default, PDF only when requested.
- Tenancy agreements follow `assets/templates/property/monthly-tenancy-english-v1.md`: preserve the current source language (English by default), use the approved Helvetica layout, and leave 200 pt (about 70.6 mm, four-to-five fingers) blank at the top of EVERY page. This is an explicit exception to petition-only first-page spacing and general English font defaults. Never assume Hindi or reuse example rent, dates or client details.
- Current user instructions override defaults and templates. For limited edits preserve unrelated established formatting.
- English: **Times New Roman, 12 pt by default**. If that font is unavailable, **Tinos** is the approved Times-compatible fallback. Never default to Courier; use Courier New only if explicitly requested as typewriter/traditional Courier style. A request for the traditional deed layout means the Times-style deed layout unless the user asks for Courier.
- Hindi: approved Noto Sans Devanagari regular/bold with DejaVu Sans for Latin/digits, 11 pt, line-height 1.6. Use bundled Hindi CSS and renderer. Do not apply English fonts to Hindi.
- A4 portrait. Every new court petition/application/affidavit/written argument gets approximately three fingers of total blank space at the top of page ONE only. Use 45 mm as a reproducible approximation, not an official measurement. Later pages: 25 mm top margin. User can remove or change the gap. For family partition deeds and other instruments, follow the supplied approved/sample layout; do not automatically impose petition-only signature spacing.
- Administrative `सेवा में` letters use the approved letter layout with normal 25 mm top margin unless the user requests the petition gap. This salutation does not by itself make a document an FIR.
- No separate Prayer heading. Indent the whole prayer toward the right for court petitions; keep the conventional closing line at normal left alignment.
- Bold verified case citations in arguments. Do not add a Conclusion heading when continuing numbered arguments. Write the case caption once.
- PDF-first: when a PDF is requested, produce it in the same turn without a DOCX-first approval cycle. Retain an editable source; provide DOCX only when asked. Text approval is not a prerequisite for providing a review PDF.

## Accuracy and speed
- Read all attached pages of the current matter directly using native image understanding before drafting; follow `skills/intake-and-ocr/SKILL.md`. Verify critical fields against visible source lines, preserve negations and relationships, and flag unclear details instead of guessing. No external OCR unless explicitly requested. Keep separate matters separate; examples control style, not new-case facts.
- Verify critical names, relationships, numbers, dates, amounts and relief against source pages. Crop/zoom only ambiguous regions. Do not guess; ask only material unresolved questions.
- Treat supplied legal samples as **format-only** unless specifically told to transfer facts. Do not copy sample parties, land particulars, dates, signatories, title history or witness names into a new matter.
- Improve Hindi grammar without changing facts, allegations, certainty or requested relief. Do not add unprovided facts such as lack of partition.
- Execute the known renderer directly. Do not run routine package/version/font inventories, browse for fonts or compare PDF engines. Reuse successful setup in the same environment. Repair only an actual missing dependency or rendering failure; environments can reset.
- One focused factual/layout review, one render of all final pages. Re-render only to repair a visible defect. A successful script is not sufficient proof of readable text.
- Do not file, sign, send or publish client documents without explicit authorization.

## Available templates
- Monthly tenancy agreement: `assets/templates/property/monthly-tenancy-english-v1.md`, user-approved 2026-09-30. Default format for tenancy/rent agreement requests; current-source facts and language control.
- Cause-list layout and reusable visual prompt: `skills/daily-cause-list/SKILL.md`. User-provided CSV/case rows are the source of truth.
- Hindi administrative application/representation: `assets/templates/hindi/seva-mein-application.json` with `assets/styles/hindi.css`.
- Family partition deed: follow `skills/family-partition-deed/SKILL.md` for reusable structural guidance; a supplied deed/photo is not automatically an advocate-approved template.
- For other matter types use a supplied approved format or prepare a first draft. Do not search nonexistent template paths.
