# Legal Petition Drafter Router

This is the first and authoritative entry point for ChatGPT and Codex when using this plugin.

## Core operating rules

1. Identify whether the user wants a simple edit, a substantive revision, a new draft, legal research, or final PDF generation.
2. Read every PDF, image, DOCX, and note supplied for the current matter directly with native file and image understanding.
3. Do not run external OCR for ordinary PDFs, scans, or photographs. If a page is genuinely unreadable, identify the exact file/page and ask for a clearer copy.
4. Verify critical names, dates, case numbers, police-station details, statutory sections, amounts, and requested relief against the original page before relying on them.
5. Never invent facts, authorities, quotations, procedural history, or missing text.
6. Load only the skills and approved template needed for the identified route.

## Routing table

| User request | Skills to load | Execution route |
|---|---|---|
| Minor text, font, spacing, alignment, or formatting change to an existing document | `skills/petition-drafter/SKILL.md`, then `skills/quality-check/SKILL.md`; add `skills/court-pdf-generator/SKILL.md` only if PDF is requested | Use the existing editable document. Change only the requested items and preserve everything else. |
| Substantive revision using supplied case records | `skills/intake-and-ocr/SKILL.md`, `skills/petition-drafter/SKILL.md`, `skills/quality-check/SKILL.md` | Read all relevant records directly, verify the fact sheet, and revise the existing draft without unnecessary redesign. |
| New petition/application | `skills/intake-and-ocr/SKILL.md`, `skills/template-manager/SKILL.md`, `skills/petition-drafter/SKILL.md`, `skills/quality-check/SKILL.md` | Read all supplied records directly and load only the matching approved template. |
| Anticipatory bail | New-draft route; add `skills/legal-research/SKILL.md` when current law or authorities are needed | `assets/templates/criminal/anticipatory-bail*.md` |
| Regular bail | New-draft route; add legal research when needed | `assets/templates/criminal/regular-bail*.md` |
| Criminal revision | New-draft route; add legal research when needed | `assets/templates/criminal/criminal-revision*.md` |
| Writ petition | New-draft route plus `skills/legal-research/SKILL.md` | `assets/templates/high-court/writ-petition*.md` |
| Police complaint or representation | Direct intake, template manager, petition drafter, and quality check | Matching approved complaint or representation template |
| Legal research only | `skills/legal-research/SKILL.md` | No template unless drafting is also requested |
| Final court PDF | `skills/court-pdf-generator/SKILL.md` plus the drafting skill already used | Preserve the selected approved template and existing layout |
| Save or update a reusable template | `skills/template-manager/SKILL.md` | Act only on explicit instruction and remove confidential case-specific facts |

## Fast path for simple edits

1. Open the existing DOCX whenever available.
2. Change only the text or formatting expressly requested.
3. Preserve all unrelated wording, numbering, margins, page breaks, fonts, alignment, and advocate-specific styling.
4. Do not re-read unrelated evidence or repeat legal research for a purely mechanical edit.
5. Export a normal searchable and selectable PDF. Do not flatten the document into page images.
6. Render and inspect once. Repeat only if an actual defect is found.

## Default court-document formatting

Unless the user or an approved template requires otherwise:

- Use Courier New for the traditional court-document style.
- Leave approximately a four-finger blank space at the top of the first page for court use or signature.
- Place the prayer text toward the right side without a separate `Prayer` heading.
- Return the conventional closing line to normal document alignment after the prayer.
- Keep the PDF text searchable and selectable.

## Template selection rules

1. GitHub is the source of truth for reusable drafting style and approved formats.
2. Prefer an exact document-type match over a generic practice-area template.
3. Match matter type, court, jurisdiction, and language.
4. Use only templates whose status is `approved` for approved-format drafting.
5. If no approved template exists, say so and create a clearly labelled first draft.
6. Never treat ordinary uploaded case papers as reusable templates.
7. Save or update a reusable template only on explicit instruction through the template-manager workflow.

## Repository map

- `skills/intake-and-ocr/SKILL.md` — read supplied records directly and build a verified fact sheet.
- `skills/template-manager/SKILL.md` — select, propose, approve, version, and retire templates.
- `skills/petition-drafter/SKILL.md` — draft or minimally edit the document.
- `skills/legal-research/SKILL.md` — conduct source-led legal research and verify authorities.
- `skills/quality-check/SKILL.md` — review facts, structure, citations, language, and layout.
- `skills/court-pdf-generator/SKILL.md` — produce and verify the final editable document and PDF.
- `assets/templates/` — advocate-approved reusable templates only.

## Substantive drafting workflow

1. Read this router.
2. Determine the document type and whether the request is a simple edit or substantive drafting.
3. Load only the routed skills and matching approved template.
4. Read every supplied case record directly.
5. Build and verify the fact sheet against the original pages.
6. Ask only targeted questions whose answers would materially affect the draft.
7. Research current law only when required.
8. Draft or revise while preserving the approved format.
9. Run one focused quality review.
10. Produce the editable output and PDF when requested.

Do not hunt through unrelated skills or template folders after the route has been resolved.
