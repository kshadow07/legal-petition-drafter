# Legal Petition Drafter Router

This is the single entry point for ChatGPT and Codex when using this plugin.

## Start here

Do not scan the repository blindly. First identify the user's intent and matter type, then load only the relevant skill files and the matching approved template.

## Routing table

| User request | Skills to load | Template route |
|---|---|---|
| Draft or revise a petition/application | `skills/intake-and-ocr/SKILL.md`, `skills/template-manager/SKILL.md`, `skills/petition-drafter/SKILL.md`, `skills/quality-check/SKILL.md` | Load only the matching approved template under `assets/templates/`. |
| Anticipatory bail | Drafting route above; add `skills/legal-research/SKILL.md` when current law or authorities are needed | `assets/templates/criminal/anticipatory-bail*.md` |
| Regular bail | Drafting route above; add legal research when needed | `assets/templates/criminal/regular-bail*.md` |
| Criminal revision | Drafting route above; add legal research when needed | `assets/templates/criminal/criminal-revision*.md` |
| Writ petition | Drafting route above plus `skills/legal-research/SKILL.md` | `assets/templates/high-court/writ-petition*.md` |
| Police complaint / representation | Intake, template manager, petition drafter, quality check | Matching approved complaint/representation template |
| Legal research only | `skills/legal-research/SKILL.md` | No template unless drafting is also requested |
| Final court PDF | `skills/court-pdf-generator/SKILL.md` plus the drafting skill already used | Preserve the selected approved template/layout |
| Save a reusable template | `skills/template-manager/SKILL.md` | Create/propose the matter-specific template; approve only on explicit instruction |
| Update an approved template | `skills/template-manager/SKILL.md` | Compare against the current approved template and update only on explicit instruction |

## Template selection rules

1. GitHub is the source of truth for reusable drafting style and approved formats.
2. Prefer an exact document-type match over a generic practice-area template.
3. Match matter type, court, jurisdiction, and language.
4. Use only templates whose status is `approved` for approved-format drafting.
5. If no approved template exists, say so and create a clearly labelled first draft instead of pretending an approved format exists.
6. Never treat ordinary uploaded case papers as reusable templates.
7. When the user explicitly says “save this as an approved template” or equivalent, use the template-manager workflow, remove case-specific/confidential facts, and create or update the appropriate template file.

## Repository map

- `skills/intake-and-ocr/SKILL.md` — extract and normalize facts from current case material.
- `skills/template-manager/SKILL.md` — select, propose, approve, version, and retire templates.
- `skills/petition-drafter/SKILL.md` — draft from verified facts using the selected approved format.
- `skills/legal-research/SKILL.md` — source-led legal research and authority verification.
- `skills/quality-check/SKILL.md` — factual, structural, citation, and drafting review.
- `skills/court-pdf-generator/SKILL.md` — produce the final court document/PDF.
- `assets/templates/` — advocate-approved reusable templates only.

## Default drafting execution

1. Read this router.
2. Determine the matter/document type.
3. Load only the routed skills.
4. Load only the matching approved template.
5. Read the user's current case documents.
6. Build and verify the fact sheet.
7. Research current law when required.
8. Draft according to the selected template.
9. Run quality review.
10. Produce editable output and then PDF when requested.

Do not hunt through unrelated skills or template folders after the route has been resolved.
