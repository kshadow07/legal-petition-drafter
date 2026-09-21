---
name: petition-drafter
description: Prepare lawyer-reviewable petition drafts using approved templates and a verified fact sheet.
---

# Petition Drafter

## Router dependency

Always start from `../../AGENTS.md`. Use the router to load only the relevant skills and the matching approved template. Do not search through unrelated skills or template folders.

## Drafting sequence

1. Confirm matter type, court, jurisdiction, language, selected template, requested output, and requested visual style.
2. Use the intake fact sheet and preserve names, dates, sections, case numbers, and quotations exactly as confirmed.
3. Follow the approved template's heading, cause title, factual chronology, grounds, prayer, verification, and signature layout.
4. Clearly identify unresolved facts and leave review markers rather than inventing text.
5. Run the routed quality-check workflow.
6. Produce an editable DOCX working draft before generating the final PDF, unless the user explicitly requests PDF-only output.
7. Treat the DOCX as the working master during review. When the user requests corrections, revise the same working draft rather than repeatedly generating new PDFs.
8. Preserve the document's current structure, formatting decisions, factual corrections, and drafting context across revisions in the same conversation. If the original DOCX is available, edit that file rather than reconstructing it from scratch.
9. Generate the final court PDF only after the user indicates that the draft is approved or asks for a final PDF.
10. If no approved template exists, label the result as a first draft and do not imply that it follows the advocate's approved house format.

## Minimal-change editing workflow

Use this fast path for routine corrections, refinements, alignment fixes, font restoration, paragraph changes, or other limited edits to an existing legal document:

1. Edit the existing DOCX directly. Do not reconstruct the document when the working DOCX is available.
2. Change only what the user requested. Preserve all unrelated text, font, font size, margins, numbering, indentation, spacing, page setup, prayer placement, signature blocks, headers, footers, and page breaks.
3. Treat the existing document as the style authority. Do not change typography or layout merely because another style appears cleaner.
4. For a normal revision, update the DOCX once, export it once as a standard text-based PDF, visually inspect the rendered pages once, and deliver both files when requested.
5. Repeat rendering only when the inspection shows a real defect. Do not expand a simple edit into redesign, font substitution, PDF flattening, or repeated conversion without a demonstrated need.
6. Keep the PDF searchable and selectable. Use image-only or flattened PDF output only when the user requests it or when a confirmed technical defect cannot otherwise be resolved.

## Visual style switch

Support two explicit presentation modes for court documents unless an approved template overrides them:

### Traditional style
Use when the user says phrases such as:
- `traditional style`
- `typewriter style`
- `old court style`
- `traditional Jamshedpur style`

Default typography:
- Font: `Courier New`
- Size: `12 pt`
- Monospaced appearance
- Conservative court-typist layout
- Avoid decorative formatting
- Preserve conventional spacing, dotted party alignment, and restrained emphasis

This mode is intended to approximate the traditional typewritten appearance often seen in district-court drafting. It is not to be described as an officially mandated court font unless an authoritative court rule or approved advocate template says so.

### Modern legal style
Use when the user says phrases such as:
- `modern legal style`
- `clean legal format`
- `modern court draft`
- `professional legal format`

Default typography:
- Font: `Times New Roman`
- Size: `12 pt`
- Conventional serif legal-document appearance
- Clean spacing and alignment
- Restrained bolding and underlining
- No decorative or corporate styling

### Priority rule
If an approved template specifies a different font, size, spacing, or typography, the approved template takes priority over these defaults.

If the user does not specify a style:
- use the typography of the approved template;
- if no approved template exists, use `Traditional style` by default;
- use `Modern legal style` only when the user explicitly asks for a modern, clean, professional, or Times New Roman legal format.

## Review-first document workflow

For petitions and applications that are likely to require advocate review or multiple rounds of correction, use this default workflow:

1. Draft the petition in editable DOCX format.
2. Share the DOCX for review.
3. Apply requested factual, legal, structural, and formatting corrections to the same working DOCX.
4. Keep confirmed drafting conventions consistent in later revisions, including court heading, cause-title structure, paragraph numbering, prayer placement, verification, signature blocks, margins, and typography.
5. Do not create a new PDF after every minor correction unless the user asks to inspect a PDF rendering.
6. After approval, run quality check and render the approved DOCX into the final PDF.
7. Visually inspect the final PDF for page breaks, alignment, indentation, missing text, font/rendering issues, and signature/prayer placement before delivery.

The editable draft is the source of truth for the current matter during the review cycle. The PDF is primarily the final presentation/filing artifact.

## Court drafting conventions learned from advocate review

When the user confirms a recurring house-style convention, preserve it for later revisions of the same matter and, when explicitly requested, add it to the relevant approved template or drafting instructions.

For Jamshedpur district-court drafting, confirmed conventions currently include:

- Leave approximately a four-finger blank space at the top of the first page before the court heading, unless the approved template or the user directs otherwise. Apply this to new petitions, applications, written arguments, affidavits, and similar court documents.
- In the prayer portion, do not automatically insert a separate heading titled `PRAYER` when the advocate's format does not use one.
- The substantive prayer text may be set inward toward the right side of the page using an appropriate left indent, following the advocate's preferred court style.
- The conventional closing line, for example, `And for this act of kindness, the petitioner as in duty bound shall ever pray.`, should return to the normal body alignment and should not inherit the prayer indentation.
- Preserve such layout rules in the editable master so the final PDF reflects them consistently.

Do not generalize a matter-specific preference into every jurisdiction or document type unless the advocate explicitly approves it as a reusable template rule.

## Court context

Default context is Jamshedpur district-court practice for criminal, civil, and family matters. Ranchi High Court drafting is a separate context: confirm jurisdiction and the applicable approved format before using it.

## Bilingual drafting

- Draft entirely in the requested language unless the approved template explicitly mixes languages.
- In Hindi, preserve Devanagari characters, names, dates, FIR numbers, and legal provisions exactly.
- Retain English statutory citations where the advocate's approved format requires them.

## Guardrails

Do not state that a court will grant relief. Do not submit, file, sign, or send a petition without the advocate's explicit direction.
