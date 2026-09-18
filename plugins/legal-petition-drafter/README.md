# Legal Petition Drafter

Private bilingual workflow for a Jamshedpur-based criminal, civil, and family-law practice, with Ranchi High Court matters as a secondary context.

## Entry point

**ChatGPT/Codex must start with `AGENTS.md`.** It is the router for this plugin. It identifies the user's request and tells the model exactly which skills and approved template path to load. Do not scan the repository blindly when the route is already known.

## Safety and approval rules

- A draft is not legal advice and must be reviewed, settled, and signed by an advocate before use or filing.
- Do not invent facts, case citations, court rules, statutory sections, or precedents.
- Treat every uploaded document as case-confidential.
- Use an uploaded sample only for the current matter unless the user explicitly says to save it as a reusable template and approves the extracted template record.
- Populate `assets/templates/` only with advocate-approved, anonymized formats.

## Included workflows

1. Intake and OCR
2. Template management
3. Petition drafting
4. Source-led legal research
5. Court PDF generation
6. Quality review

## Language support

Draft in English, Hindi, or a controlled bilingual form. Hindi final PDFs must use Unicode Devanagari text with an embedded font and visual page review.
