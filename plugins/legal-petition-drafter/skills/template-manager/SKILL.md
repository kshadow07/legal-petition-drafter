---
name: template-manager
description: Select, propose, and maintain advocate-approved legal document templates without accidental template saving.
---

# Template Manager

## Router dependency

Start from `../../AGENTS.md` and follow its routing and template-selection rules. Once the matter type is known, do not scan unrelated template folders.

## Template states

- `unapproved`: uploaded sample or one-off case document; usable only as a current-draft reference.
- `proposed`: fields, sections, and drafting notes extracted for the advocate to inspect.
- `approved`: reusable format explicitly approved by the advocate.
- `retired`: preserved for history but not selected for new drafts.

## Rules

1. Never move an uploaded document to `approved` automatically.
2. When asked to "add this template", first create a proposed template record showing title, document type, jurisdiction, language, court heading, sections, variable fields, date/version, and source file.
3. Save it as approved only after an explicit instruction such as "Approve and save this template" or "Save this as an approved template".
4. When drafting, select only an approved template matching the requested matter, court, jurisdiction, and language.
5. If no approved template exists, say so and prepare a clearly labelled first draft rather than pretending it is an approved format.
6. Strip client-specific and confidential facts before creating a reusable template.
7. Use deterministic folders and filenames, for example `assets/templates/criminal/criminal-revision-v1.md`.
8. Prefer exact document-type matches before broader practice-area matches.
9. When updating an approved template, preserve version/date metadata and rely on Git history for the previous version.

## Template metadata

Every reusable approved template should identify at least:

- `template_id`
- `document_type`
- `practice_area`
- `jurisdiction`
- `court_level`
- `language`
- `status: approved`
- `version`
- `approved_date`

## Template inventory

Template folders may remain empty until advocate-approved examples are supplied. Do not fabricate placeholder legal formats merely to populate the inventory.
