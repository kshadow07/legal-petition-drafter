"""Render verified plain-text matter JSON using the approved Hindi layout."""
import argparse
import html
import json
import re
from pathlib import Path
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

ROOT = Path(__file__).resolve().parents[1]

def render(data, output):
    for name in ('Regular', 'Bold'):
        font = ROOT / 'assets/fonts' / f'NotoSansDevanagari-{name}.ttf'
        if not font.is_file():
            raise FileNotFoundError(f'Restore bundled font: {font}')
    for field in ('subject', 'prayer', 'applicant_name'):
        if not isinstance(data.get(field), str) or not data[field].strip():
            raise ValueError(f'Missing text field: {field}')
    for field in ('recipient', 'paragraphs', 'applicant_details', 'copies', 'emphasis'):
        if not isinstance(data.get(field, []), list) or not all(isinstance(v, str) for v in data.get(field, [])):
            raise ValueError(f'{field} must be a list of plain-text strings')
    kind = data.get('document_kind', 'letter')
    if kind not in ('letter', 'petition'):
        raise ValueError('document_kind must be letter or petition')
    size = float(data.get('font_size_pt', 11))
    page_top = float(data.get('page_top_mm', 85))
    top = float(data.get('first_page_top_mm', page_top))
    if not 8 <= size <= 24 or not 10 <= top <= 100 or not 10 <= page_top <= 100:
        raise ValueError('Invalid font size or first-page margin')
    terms = sorted(set(x for x in data.get('emphasis', []) if x), key=len, reverse=True)
    pattern = re.compile('(' + '|'.join(map(re.escape, terms)) + ')') if terms else None
    def esc(value):
        return html.escape(str(value), quote=True)
    def text(value):
        value = str(value)
        if not pattern:
            return esc(value)
        return ''.join('<strong>'+esc(s)+'</strong>' if i%2 else esc(s) for i,s in enumerate(pattern.split(value)))
    recipient = '<br>'.join(esc(x) for x in data.get('recipient', []))
    facts = ''.join(f'<p>{i}. {text(v)}</p>' for i,v in enumerate(data.get('paragraphs', []), 1))
    details = '<br>'.join(esc(x) for x in data.get('applicant_details', []))
    copies = ''
    if data.get('copies'):
        copies = '<div class="copy-to"><strong>प्रतिलिपि सूचनार्थ एवं आवश्यक कार्रवाई हेतु प्रेषित:</strong><br>' + '<br>'.join(f'{i}. {esc(v)}' for i,v in enumerate(data['copies'], 1)) + '</div>'
    greeting = '' if kind == 'petition' else '<strong>सेवा में,</strong><br>'
    source = f'''<!DOCTYPE html><html lang="hi"><head><meta charset="UTF-8">
<link rel="stylesheet" href="{(ROOT/'assets/styles/hindi.css').as_uri()}">
<style>@page {{ margin-top: {page_top}mm; }} @page :first {{ margin-top: {top}mm; }} body {{ font-size: {size}pt; }}</style></head>
<body class="{kind}"><div class="header">{greeting}{recipient}</div>
<div class="subject">{esc('विषय: ' if kind == 'letter' else '')}{esc(data['subject'])}</div>
<div class="salutation"><strong>{esc(data.get('salutation', ''))}</strong></div>
<div class="content">{text(data.get('introduction', ''))}</div>
<div class="content">{text(data.get('facts_heading', ''))}</div>
<div class="facts">{facts}</div>
<div class="prayer"><strong>{esc(data.get('prayer_opening', 'अतः श्रीमान से नम्र निवेदन है'))}</strong> {text(data['prayer'])}</div>
<div class="closing">{text(data.get('closing', ''))}</div>
<div class="signatures"><div class="date-place"><strong>दिनांक:</strong> {esc(data.get('date', '....................'))}<br><strong>स्थान:</strong> {esc(data.get('place', '....................'))}</div>
<div class="sign-block">{esc(data.get('signoff', 'भवदीय,'))}<br><br><br><strong>({esc(data['applicant_name'])})</strong><br>{details}</div></div>{copies}</body></html>'''
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    editable = output.with_suffix('.html')
    editable.write_text(source, encoding='utf-8')
    HTML(filename=str(editable)).write_pdf(str(output), font_config=FontConfiguration())
    return output

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('matter_json', type=Path)
    parser.add_argument('output_pdf', type=Path)
    parser.add_argument('--html', action='store_true', help='Input is structured court HTML, not the simple JSON layout')
    parser.add_argument('--no-first-page-gap', action='store_true', help='Explicitly reduce first-page top margin to 25 mm; continuation pages retain the saved default')
    args = parser.parse_args()
    if args.html:
        for weight in ('Regular', 'Bold'):
            if not (ROOT/'assets/fonts'/f'NotoSansDevanagari-{weight}.ttf').is_file():
                raise FileNotFoundError('Restore bundled Hindi fonts')
        args.output_pdf.parent.mkdir(parents=True, exist_ok=True)
        config = FontConfiguration()
        HTML(filename=str(args.matter_json)).write_pdf(str(args.output_pdf), stylesheets=[CSS(filename=str(ROOT/'assets/styles/hindi.css'), font_config=config), CSS(string='@page :first { margin-top: ' + ('25' if args.no_first_page_gap else '85') + 'mm; }', font_config=config)], font_config=config)
        print(args.output_pdf)
        raise SystemExit(0)
    print(render(json.loads(args.matter_json.read_text(encoding='utf-8')), args.output_pdf))
