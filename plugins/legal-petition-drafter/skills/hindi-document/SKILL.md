---
name: hindi-document
description: Create or revise Hindi legal PDFs, petitions and seva-mein administrative applications using the approved Hindi typography, HTML/CSS layout and WeasyPrint renderer.
---

Read `../../AGENTS.md` once if not already loaded. Reuse its Jamshedpur practice context.

## Direct route
1. Read current source pages natively; verify names and numbers. Keep facts separate from style examples. Ask only for material unreadable details.
2. For an administrative letter, copy `../../assets/templates/hindi/seva-mein-application.json` to the current matter's working directory and fill it with confirmed facts. The template is an approved layout, not legal authority or an FIR form. The JSON renderer is suitable only for this simple layout or a simple petition that fits its fields. For court captions, affidavits, verification, unnumbered sections or other supplied structures, preserve them in UTF-8 HTML with `<body class="petition">` and run `python scripts/generate_hindi_pdf.py court.html output.pdf --html` (add `--no-first-page-gap` if requested). Apply the same bundled CSS; do not force a court document into the letter schema.
3. Use clear Hindi: e.g. `सविनय निवेदन है कि`, `प्रार्थी का कथन संक्षेप में निम्नवत है:`. Preserve factual certainty and relief. Do not add facts or expand a stay request into cancellation without instruction. Do not mechanically copy ornate phrases or sample party names.
4. Execute directly from the plugin root: `python scripts/generate_hindi_pdf.py matter.json output.pdf`. JSON strings are plain text, never HTML. Fields in `emphasis` are exact, verified phrases to bold (such as a case number); the subject, salutation, prayer opening, applicant name and copy heading already have controlled bolding.
5. For JSON mode edit JSON as the master; its emitted HTML is regenerated and overwritten. For HTML mode edit the source HTML directly. Retain the master for quick corrections; deliver the PDF first. No DOCX detour unless requested. For a mechanical change edit the saved source and regenerate once.
6. Inspect every page once. Check conjuncts/matras, sensible Hindi/Latin balance, paragraph spacing and signatures. Do not blindly tune fonts or run additional checks when the output is correct.

## Approved design
- Preserve the user's demonstrated HTML/WeasyPrint appearance: Noto Sans Devanagari regular/bold for Hindi, DejaVu Sans for Latin/digits, 11 pt body and 1.6 line height. Use `assets/styles/hindi.css` rather than inventing CSS each time.
- A4; top/bottom/left 25 mm, right 20 mm for administrative letters. A petition defaults to 45 mm TOTAL top margin on page one only; later pages remain 25 mm. This approximates three fingers. `first_page_gap: false` removes the special petition gap; `first_page_top_mm` allows an explicit adjustment.
- Preserve numbered paragraphs, bold subject and prayer opening, right signature and normal closing. Letter prayer matches the approved first-line indent; court-petition prayer indents the whole paragraph with no separate heading.
- For an explicitly requested larger font use `font_size_pt`; do not change the approved 11 pt default unnecessarily.

## Runtime recovery, only on failure
Run the renderer first; it imports WeasyPrint directly and verifies its two required local font files. No version query. If WeasyPrint is absent, install that missing package once in the active Python environment. If bundled fonts are missing, retrieve `assets/fonts/NotoSansDevanagari-Regular.ttf` and `NotoSansDevanagari-Bold.ttf` from this repository. If DejaVu Sans is absent, install it once or disclose the substitution. Do not download fonts or dependencies on every run. Never claim packages persist across fresh environments.
