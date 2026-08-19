from __future__ import annotations

from pathlib import Path
import re
import html
import mistune
from bs4 import BeautifulSoup
from weasyprint import HTML

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / 'PAPER.md'
OUT = ROOT / 'paper'
OUT.mkdir(parents=True, exist_ok=True)

md = PAPER.read_text(encoding='utf-8')
renderer = mistune.HTMLRenderer(escape=False)
markdown = mistune.create_markdown(renderer=renderer, plugins=['table', 'strikethrough'])
body_html = markdown(md)
soup = BeautifulSoup(body_html, 'html.parser')

# Stable unique IDs and TOC.
seen: dict[str, int] = {}
toc_items: list[tuple[int, str, str]] = []
for heading in soup.find_all(re.compile(r'^h[1-3]$')):
    text = heading.get_text(' ', strip=True)
    slug = re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-') or 'section'
    n = seen.get(slug, 0)
    seen[slug] = n + 1
    if n:
        slug = f'{slug}-{n+1}'
    heading['id'] = slug
    level = int(heading.name[1])
    if level >= 2:
        toc_items.append((level, text, slug))

# First H1 becomes title masthead; the source H2 is subtitle.
first_h1 = soup.find('h1')
subtitle = first_h1.find_next_sibling('h2') if first_h1 else None
if first_h1:
    first_h1['class'] = ['paper-title']
if subtitle:
    subtitle['class'] = ['paper-subtitle']

# Add semantic classes.
for table in soup.find_all('table'):
    table['class'] = (table.get('class') or []) + ['data-table']
for pre in soup.find_all('pre'):
    pre['class'] = (pre.get('class') or []) + ['code-block']
for blockquote in soup.find_all('blockquote'):
    blockquote['class'] = (blockquote.get('class') or []) + ['pull-quote']

# Linked TOC with indentation.
toc = ['<nav class="toc" aria-label="Table of contents">', '<h2>Contents</h2>', '<ol>']
for level, text, slug in toc_items:
    toc.append(f'<li class="toc-l{level}"><a href="#{slug}">{html.escape(text)}</a></li>')
toc.extend(['</ol>', '</nav>'])

css = r'''
:root {
  --ink: #17202a;
  --muted: #52606d;
  --line: #d8dee6;
  --soft: #f5f7fa;
  --accent: #183b56;
  --accent-2: #2f6b8a;
  --paper: #ffffff;
  --max: 860px;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  color: var(--ink);
  background: #eef1f4;
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Arial, sans-serif;
  font-size: 17px;
  line-height: 1.68;
  text-rendering: optimizeLegibility;
}
a { color: var(--accent-2); text-decoration-thickness: 1px; text-underline-offset: 2px; }
a:hover { color: var(--accent); }
.site-header {
  position: sticky; top: 0; z-index: 10;
  border-bottom: 1px solid var(--line);
  background: rgba(255,255,255,.96);
  backdrop-filter: blur(8px);
}
.site-header-inner {
  max-width: 1180px; margin: 0 auto; padding: 12px 22px;
  display: flex; justify-content: space-between; gap: 20px; align-items: center;
}
.brand { font-size: 14px; font-weight: 750; letter-spacing: .02em; color: var(--accent); }
.meta-links { display: flex; gap: 16px; font-size: 13px; }
.layout {
  max-width: 1180px; margin: 0 auto; padding: 34px 22px 70px;
  display: grid; grid-template-columns: 240px minmax(0, var(--max)); gap: 42px; align-items: start;
}
.toc {
  position: sticky; top: 74px;
  max-height: calc(100vh - 94px); overflow: auto;
  padding: 18px 16px; border: 1px solid var(--line); border-radius: 10px;
  background: rgba(255,255,255,.9);
}
.toc h2 { margin: 0 0 10px; border: 0; padding: 0; font-size: 14px; text-transform: uppercase; letter-spacing: .08em; }
.toc ol { list-style: none; margin: 0; padding: 0; }
.toc li { margin: 6px 0; font-size: 13px; line-height: 1.35; }
.toc-l3 { padding-left: 13px; }
.toc a { color: var(--muted); text-decoration: none; }
.toc a:hover { color: var(--accent); }
.paper {
  background: var(--paper); border: 1px solid var(--line); border-radius: 12px;
  padding: 62px 66px 72px; box-shadow: 0 12px 35px rgba(24,59,86,.06);
}
.paper-title {
  margin: 0; color: var(--accent); font-family: Georgia, "Times New Roman", serif;
  font-size: 48px; line-height: 1.06; letter-spacing: -.025em;
}
.paper-subtitle {
  margin: 15px 0 31px; padding: 0 0 28px; border-bottom: 2px solid var(--accent);
  color: var(--muted); font-family: Georgia, "Times New Roman", serif;
  font-size: 23px; line-height: 1.34; font-weight: 400;
}
h2, h3 { scroll-margin-top: 88px; }
h2 {
  margin: 2.35em 0 .65em; padding-bottom: .25em; border-bottom: 1px solid var(--line);
  color: var(--accent); font-family: Georgia, "Times New Roman", serif;
  font-size: 30px; line-height: 1.25;
}
h3 {
  margin: 1.85em 0 .5em; color: var(--accent);
  font-family: Georgia, "Times New Roman", serif; font-size: 22px; line-height: 1.3;
}
p { margin: .8em 0; }
strong { color: #111820; }
code {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: .88em; background: var(--soft); padding: .12em .3em; border-radius: 4px;
}
pre.code-block {
  margin: 1.25em 0; padding: 18px 20px; overflow-x: auto;
  border: 1px solid var(--line); border-left: 4px solid var(--accent-2); border-radius: 7px;
  background: var(--soft); line-height: 1.48; break-inside: avoid;
}
pre code { padding: 0; background: transparent; font-size: 13px; }
.pull-quote {
  margin: 1.45em 0; padding: 14px 22px; border-left: 4px solid var(--accent-2);
  background: #f7fafc; color: #243b53; font-family: Georgia, "Times New Roman", serif;
  font-size: 19px;
}
ul, ol { padding-left: 1.45em; }
li { margin: .25em 0; }
.data-table {
  width: 100%; border-collapse: collapse; margin: 1.35em 0; font-size: 13px; line-height: 1.45;
}
.data-table th, .data-table td { border: 1px solid var(--line); padding: 9px 10px; vertical-align: top; }
.data-table th { background: #eaf0f4; text-align: left; color: var(--accent); }
.data-table tr:nth-child(even) td { background: #fafbfc; }
.footer-note {
  max-width: 860px; margin: 24px auto 0; color: var(--muted); font-size: 12px; text-align: center;
}
@media (max-width: 920px) {
  .layout { display: block; padding: 18px 12px 48px; }
  .toc { position: relative; top: auto; max-height: none; margin-bottom: 18px; }
  .paper { padding: 36px 26px 48px; }
  .paper-title { font-size: 38px; }
  .site-header-inner { padding: 10px 14px; }
}
@page {
  size: A4;
  margin: 20mm 18mm 20mm;
  @top-left { content: "Governed Agent Organizations"; color: #52606d; font-size: 8.5pt; }
  @top-right { content: "Paper v1.1"; color: #52606d; font-size: 8.5pt; }
  @bottom-center { content: counter(page); color: #52606d; font-size: 8.5pt; }
}
@media print {
  body { background: white; font-family: Georgia, "Times New Roman", serif; font-size: 10.5pt; line-height: 1.48; }
  .site-header, .toc, .footer-note { display: none; }
  .layout { display: block; margin: 0; padding: 0; max-width: none; }
  .paper { border: 0; border-radius: 0; box-shadow: none; padding: 0; }
  .paper-title { font-size: 28pt; page-break-after: avoid; }
  .paper-subtitle { font-size: 15pt; margin-bottom: 22pt; }
  h2 { font-size: 17pt; break-after: avoid; margin-top: 19pt; }
  h3 { font-size: 13pt; break-after: avoid; margin-top: 14pt; }
  p, li { orphans: 3; widows: 3; }
  a { color: inherit; text-decoration: none; }
  pre.code-block { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 8pt; white-space: pre-wrap; }
  .data-table { font-family: Arial, sans-serif; font-size: 7.6pt; }
  .data-table th, .data-table td { padding: 5pt; }
  blockquote { break-inside: avoid; }
}
'''

# Public links intentionally point only to public-safe files/repos.
html_doc = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="A governed architecture for persistent AI agent organizations: identity, context continuity, memory, authority, evidence, and outcomes as separate layers.">
<title>Governed Agent Organizations - Paper v1.1</title>
<style>{css}</style>
</head>
<body>
<header class="site-header"><div class="site-header-inner">
  <div class="brand">Governed Agent Organizations</div>
  <div class="meta-links">
    <a href="../CLAIM-EVIDENCE-LEDGER.csv">Claims</a>
    <a href="../SOURCE-AND-LICENSE-REGISTRY.csv">Sources</a>
    <a href="../LIMITATIONS-AND-NON-CLAIMS.md">Limitations</a>
  </div>
</div></header>
<div class="layout">
{''.join(toc)}
<main class="paper" id="paper">{str(soup)}</main>
</div>
<div class="footer-note">Paper v1.1 - related-work correction. See the source registry, audit record, and limitations for evidence boundaries.</div>
</body></html>'''

html_path = OUT / 'index.html'
pdf_path = OUT / 'governed-agent-organizations.pdf'
html_path.write_text(html_doc, encoding='utf-8')
HTML(string=html_doc, base_url=str(OUT)).write_pdf(
    str(pdf_path),
    presentational_hints=True,
    custom_metadata=True,
)
print(html_path)
print(pdf_path)
