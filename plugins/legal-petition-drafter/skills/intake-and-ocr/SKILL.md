---
name: intake-and-ocr
description: Read and verify case facts directly from user-supplied PDFs, scans, photographs, DOCX files, and notes for legal drafting.
---

# Document Intake

Use this skill before substantive drafting when source documents are supplied. The folder name is retained for compatibility; external OCR is not the default workflow.

## Direct-reading rule

Read every supplied PDF, image, DOCX file, and note directly with native file and image understanding. Do not run external OCR for ordinary PDFs, scans, or photographs. If a page is genuinely unreadable, identify the exact file/page and ask the user for a clearer copy.

## Procedure

1. Inventory every supplied file and all of its pages.
2. Read every relevant document directly without inferring text or facts that are not visible.
3. Preserve the source language. Retain Hindi in Unicode Devanagari rather than transliterating it.
4. Create a fact sheet covering jurisdiction, court, matter type, parties, relationships, case/FIR/complaint number, police station, dates and times, chronology, cited sections, evidence, procedural history, relief, and known deadlines.
5. Check critical names, dates, case numbers, police-station details, statutory sections, amounts, and relief against the original page.
6. Mark each fact as `source-confirmed`, `client-provided`, `conflicting`, or `missing`.
7. Ask only targeted questions about missing or conflicting facts that would materially affect the draft.

## Guardrails

- The original document page controls if extracted or remembered text differs from it.
- Do not invent obscured words or silently fill gaps.
- Do not convert a scanned signature, seal, or letterhead into a reusable asset.
- Do not determine an offence, claim, limitation period, or legal strategy from document extraction alone.
