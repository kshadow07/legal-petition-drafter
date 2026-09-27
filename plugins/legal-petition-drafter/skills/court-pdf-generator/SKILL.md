---
name: court-pdf-generator
description: Export requested legal PDFs promptly with searchable text and one visual check, using the existing source or bundled Hindi renderer.
---

Follow `../../AGENTS.md`. Requested PDF delivery does not require prior advocate approval of the text. Filing/signing/sending is separate.

- Hindi: use `../hindi-document/SKILL.md` and `../../scripts/generate_hindi_pdf.py`; retain JSON/HTML as editable source. Do not route through DOCX unless requested or needed to preserve an existing DOCX layout.
- English: preserve the existing editable source; default to Times New Roman 12 pt. Export directly with the already working converter. If none has been established, run `libreoffice -env:UserInstallation=file:///tmp/legal-lo-profile --headless --convert-to pdf --outdir OUTPUT_DIR INPUT.docx` directly; diagnose/install only after an actual command failure. For a new DOCX use python-docx, set English run fonts to Times New Roman and use 25 mm page-top margins plus a one-time 20 mm spacer before the first heading (never a repeating header spacer); inspect the exported first/second pages. Do not substitute another font silently if Times New Roman is unavailable.
- Court petitions: A4; approximately three fingers (45 mm total top margin) on page one only, 25 mm on later pages. Administrative letters normally use 25 mm throughout. Respect user overrides.
- Keep regular/bold fonts embedded, text selectable, prayer/closing alignment intact, and signature blocks together when they fit on a page.
- Run the known conversion directly. Never query versions or reinstall functioning dependencies. If execution fails, repair only that missing component and reuse it thereafter.
- Render every output page once using `render_pdf.py` or the available PDF renderer. Inspect Hindi matras/conjuncts, bolding, line wrapping, page breaks, margins and signatures. Fix actual defects only.
