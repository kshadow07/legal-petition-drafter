# Legal Petition Drafter: start here

Default practice: the user's father works at Jamshedpur district court, East Singhbhum, Jharkhand. Use this context without asking again; never infer a particular judge, case number, or jurisdiction against the supplied records.

## Routes
Read this file once per task, then only the needed skill. Reuse files already read in the same task. Do not scan the repository or load every skill.

| Request | Load next |
| --- | --- |
| Hindi draft or Hindi PDF | `skills/hindi-document/SKILL.md` |
| English draft or substantive revision | `skills/petition-drafter/SKILL.md` |
| Read handwritten/image case records | Add `skills/intake-and-ocr/SKILL.md` |
| Mechanical edit | Existing editable source; load only the language skill if needed; skip unrelated evidence and research |
| Current law or citations required | Add `skills/legal-research/SKILL.md` |
| Manage reusable templates | `skills/template-manager/SKILL.md` |
| PDF export or layout issue | `skills/court-pdf-generator/SKILL.md` |

## Authoritative defaults
- Current user instructions override defaults and templates. For limited edits preserve unrelated established formatting.
- English: Times New Roman, 12 pt. Courier New only when explicitly requested as traditional/typewriter style.
- Hindi: approved Noto Sans Devanagari regular/bold with DejaVu Sans for Latin/digits, 11 pt, line-height 1.6. Use the bundled Hindi CSS and renderer. Do not substitute Noto Serif or apply English fonts to Hindi.
- A4 portrait. Every new court petition/application/affidavit/written argument gets approximately three fingers of total blank space at the top of page ONE only. Use 45 mm as a reproducible approximation, not an official measurement. Later pages: 25 mm top margin. User can remove or change the gap.
- Administrative `सेवा में` letters use the approved letter layout with normal 25 mm top margin unless the user requests the petition gap. This salutation does not by itself make a document an FIR.
- No separate Prayer heading. Indent the whole prayer toward the right for court petitions; keep the conventional closing line at normal left alignment.
- Bold verified case citations in arguments. Do not add a Conclusion heading when continuing numbered arguments. Write the case caption once.
- PDF-first: when a PDF is requested, produce it in the same turn without a DOCX-first approval cycle. Retain an editable source; provide DOCX only when asked. Text approval is not a prerequisite for providing a review PDF.

## Accuracy and speed
- Read all relevant supplied pages directly with native vision. No external OCR unless explicitly requested. Keep separate matters separate; examples control style, not new-case facts.
- Verify critical names, relationships, numbers, dates, amounts and relief against source pages. Crop/zoom only ambiguous regions. Do not guess; ask only material unresolved questions.
- Improve Hindi grammar without changing facts, allegations, certainty or requested relief. Do not add unprovided facts such as lack of partition.
- Execute the known renderer directly. Do not run routine package/version/font inventories, browse for fonts or compare PDF engines. Reuse successful setup in the same environment. Repair only an actual missing dependency or rendering failure; environments can reset.
- One focused factual/layout review, one render of all final pages. Re-render only to repair a visible defect. A successful script is not sufficient proof of readable text.
- Do not file, sign, send or publish client documents without explicit authorization.

## Available templates
- Hindi administrative application/representation: `assets/templates/hindi/seva-mein-application.json` with `assets/styles/hindi.css`.
- For other matter types use a supplied approved format or prepare a first draft. Do not search nonexistent template paths.
