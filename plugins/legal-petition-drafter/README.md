# Legal Petition Drafter

Private bilingual workflow for a Jamshedpur-based criminal, civil, and family-law practice, with Ranchi High Court matters as a secondary context.

## Entry point

**ChatGPT/Codex must start with `AGENTS.md`.** It is the precise router for this plugin. It separates quick document edits from substantive drafting and tells the model which skills and approved template path to load. Do not scan the repository blindly when the route is already known.

## Safety and approval rules

- A draft is not legal advice and must be reviewed, settled, and signed by an advocate before use or filing.
- Do not invent facts, case citations, court rules, statutory sections, or precedents.
- Treat every uploaded document as case-confidential.
- Read supplied PDFs, images, DOCX files, and notes directly. Do not use external OCR for ordinary documents.
- If a page is unreadable, identify it and request a clearer copy.
- Use an uploaded sample only for the current matter unless the user explicitly asks to save it as a reusable template and approves the extracted template record.
- Populate `assets/templates/` only with advocate-approved, anonymized formats.

## Included workflows

1. Direct document intake and fact verification
2. Fast, minimal-change document editing
3. Template management
4. Petition drafting
5. Source-led legal research
6. Court PDF generation
7. Quality review

## Default document conventions

Unless the user or an approved template requires otherwise:

- Use Courier New for the traditional court-document style.
- Leave approximately a four-finger blank space at the top of the first page.
- Place the prayer toward the right without a separate `Prayer` heading.
- Keep the closing line at normal alignment.
- Produce a searchable and selectable PDF rather than flattened page images.

## Language support

Draft in English, Hindi, or a controlled bilingual form. Hindi final PDFs must use Unicode Devanagari text with an embedded font and visual page review.
