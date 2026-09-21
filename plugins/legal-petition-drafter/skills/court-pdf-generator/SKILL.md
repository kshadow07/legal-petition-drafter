---
name: court-pdf-generator
description: Produce reviewable, court-ready bilingual document outputs and visually verify the final PDF.
---

# Court PDF Generator

## Required outputs

Generate an editable source document and a PDF only after the advocate approves the draft text.

## Standard conversion workflow

1. Use the approved or corrected DOCX as the source of truth.
2. For a simple revision, preserve every unrequested formatting choice and export the updated DOCX directly to PDF.
3. Produce a normal text-based PDF with searchable and selectable text. Do not flatten pages into images unless the user explicitly requests it or a confirmed rendering defect requires it.
4. Perform one focused visual check of every page. Re-export only when that check reveals an actual defect.
5. Preserve the approximately four-finger blank space above the court heading on the first page when required by the Jamshedpur house style.
6. Preserve a right-inset prayer without a separate prayer heading when that convention is selected, and return the conventional closing line to the normal body alignment.

## Hindi requirements

- Use Unicode Devanagari text.
- Embed a licensed Devanagari font in the PDF, such as Noto Serif Devanagari when available and approved.
- Do not use image-only Hindi text or a legacy font that depends on the recipient's computer.

## Verification

1. Render every final PDF page to images.
2. Check page size, margins, heading alignment, page numbering, line wrapping, paragraph numbering, footers, signatures, and annexure references.
3. For Hindi, visually inspect matras, conjuncts, punctuation, and mixed Hindi/English lines.
4. If any glyph is missing, clipped, overlapped, or substituted, correct it before delivery.

Never send or file an output automatically. A WhatsApp or other delivery action requires the advocate's explicit confirmation of both the file and recipient.
