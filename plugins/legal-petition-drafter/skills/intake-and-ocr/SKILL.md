---
name: intake-and-ocr
description: Read all attached case-document pages directly using native image understanding and verify handwritten Hindi names, numbers, relationships and relief before legal drafting.
---

# Direct document reading

Apply before drafting from attached case records. The folder name is retained for compatibility; do not run external OCR unless the user explicitly requests it.

## Read, verify, then draft
1. Account for every attached file and page. Read every page of the current matter, including continuation pages, marginal additions and the final request. Identify separate matters and style-only references before using their contents.
2. Inspect the actual page images using native image understanding. Images visible in the conversation can be read directly without a download. For scanned PDFs, render pages for visual reading when needed. PDF text extraction may assist navigation but is not proof of what handwriting says.
3. Read the whole page for context first. Then verify critical fields against the relevant visible lines: each person's name and role, parent/spouse name, age, address, phone number, date, amount, plot/khata/case number, marital status, negations, and requested relief. Check phone numbers and identifiers digit by digit; never complete them from an expected length or familiar pattern.
4. Build a compact fact sheet with file/page references and statuses: `source-confirmed`, `client-provided`, `unclear`, `conflicting`, or `missing`. Preserve original Hindi spelling and exact digits. Distinguish a source allegation from an independently established fact.
5. If a field is unclear, inspect only that region more closely, keeping surrounding text for context. Crop, enlarge or rotate the original pixels when useful; this is not external OCR. Do not generatively redraw, reconstruct or invent obscured handwriting. If uncertainty remains, quote the readable portion and mark `[अस्पष्ट]`; ask one targeted question or request a clearer close-up for a material field.
6. Only after reading and checking the facts, rewrite into legal language. Preserve who did what, relationships, negations, dates, amounts, uncertainty and scope of relief. Do not silently normalize names, turn an unmarried person into a married one, or add facts to make a narrative sound complete.
7. Compare the drafted critical fields against the fact sheet before rendering. For a formatting-only revision, reuse already verified facts and do not repeat intake.

## Evidence boundaries
- Do not use memory, previous drafts, sample templates or another model's confident transcription to fill unreadable current-source text. Explicit user corrections are client-provided facts; keep their provenance and resolve material conflicts.
- Do not merge people or allegations from separate matters. Style examples supply formatting only.
- Treat crossed-out text as cancelled unless the user says otherwise; use a legible replacement. If correction order is ambiguous, mark it unclear.
- Do not silently reconcile conflicting numbers, areas or spellings. Preserve the competing readings with their locations.
- If an attachment path fails but the image is visible in the conversation, read that image directly. If neither image nor file can be accessed, disclose that and request access; never claim to have inspected it.
- If asked whether everything is readable, distinguish clear details from uncertainty. Do not promise complete or 100% accuracy on partly obscured pages.
- Do not reuse scanned signatures/seals as assets or infer legal strategy from transcription alone.

## Fast interaction
- If the user asks only to read or assess legibility, give the key readings and exact uncertain regions; do not draft, research or generate a PDF.
- If the user explicitly asks to confirm facts before drafting, show the compact fact sheet and wait.
- Otherwise proceed directly when material facts are clear. Ask only about unresolved material details; do not impose a routine approval round or print a full transcription unnecessarily.
- Load only the selected drafting skill after intake. Do not perform package/version checks, web searches or repeated full-document passes for straightforward image reading.
