---
name: court-pdf-generator
description: Export requested legal PDFs promptly with searchable text and one visual check, using the existing source or bundled Hindi renderer.
---

Follow `../../AGENTS.md`. Requested PDF delivery does not require prior advocate approval of the text. Filing/signing/sending is separate.

- Hindi: use `../hindi-document/SKILL.md` and `../../scripts/generate_hindi_pdf.py`; retain JSON/HTML as editable source. Do not route through DOCX unless requested or needed to preserve an existing DOCX layout.
- English: preserve the existing editable source; default to **Times New Roman, 12 pt**. If Times New Roman is unavailable, use **Tinos** as the explicit permitted fallback. Never silently use Courier or another unrelated font. Export directly with the already working converter. If none has been established, run `libreoffice -env:UserInstallation=file:///tmp/legal-lo-profile --headless --convert-to pdf --outdir OUTPUT_DIR INPUT.docx` directly; diagnose/install only after an actual command failure. For a new DOCX use python-docx, set English run fonts to Times New Roman (or Tinos fallback). Court petitions: 25 mm page-top margins plus a one-time 20 mm spacer before first heading, never a repeating header spacer. Deeds: reproduce the supplied reference layout rather than adding petition-only whitespace.
- Court petitions: A4; approximately three fingers (45 mm total top margin) on page one only, 25 mm on later pages. Administrative letters normally use 25 mm throughout. Respect user overrides.
- Family partition deeds: route to `../family-partition-deed/SKILL.md`. Centre `A N D` between party descriptions; use restrained underlined deed/schedule headings, readable body spacing, and keep witness/signature blocks **at the end, after Schedule C**. Do not import any sample-deed parties or facts. Keep signature blocks together when practicable.
- Keep regular/bold fonts embedded, text selectable, prayer/closing alignment intact, and signature blocks together when they fit on a page.
- Run the known conversion directly. Never query versions or reinstall functioning dependencies. If execution fails, repair only that missing component and reuse it thereafter.
- Render every output page once using `render_pdf.py` or the available PDF renderer. Inspect Hindi matras/conjuncts, bolding, line wrapping, page breaks, margins and signatures. Fix actual defects only.
