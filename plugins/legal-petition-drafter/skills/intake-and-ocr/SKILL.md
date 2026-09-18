---
name: intake-and-ocr
description: Extract and verify case facts from user-supplied scans, photos, PDFs, and notes for a legal draft.
---

# Intake and OCR

Use this skill before drafting when source documents are supplied.

## Procedure

1. Inventory every uploaded item without inferring facts not present in it.
2. Extract text while preserving the source language. For Hindi, retain Unicode Devanagari rather than transliteration.
3. Create a fact sheet with: jurisdiction, court, matter type, parties, relationship of parties, case/FIR/complaint number, police station, dates/times, factual chronology, sections cited in the source, evidence, requested relief, and known deadlines.
4. Mark each fact as `source-confirmed`, `client-provided`, or `missing`.
5. Ask targeted questions for missing or conflicting facts before drafting.

## Guardrails

- OCR output is evidence of text extraction, not proof of the original document's accuracy.
- Do not convert a scanned signature, seal, or letterhead into a reusable asset.
- Do not determine an offence, claim, limitation period, or legal strategy from OCR alone.
