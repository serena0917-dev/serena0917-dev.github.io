#!/usr/bin/env python3
"""
Resume Markdown → HTML (web-optimized, mirrors PDF styling)

Usage:
    uv run --with markdown build_resume_html.py

Renders ~/Documents/resume/tina-chen-resume.md to index.html
for GitHub Pages deployment.
"""

from pathlib import Path
import markdown

INPUT = Path(__file__).parent / "tina-chen-resume.md"
OUTPUT = Path(__file__).parent / "index.html"

CSS_HTML = """
:root {
    --slate-900: #0f172a;
    --slate-800: #1f2937;
    --slate-600: #475569;
    --slate-500: #64748b;
    --slate-300: #cbd5e1;
    --slate-200: #e2e8f0;
    --slate-100: #f1f5f9;
    --slate-50:  #f8fafc;
    --blue-500: #3b82f6;
    --blue-700: #1d4ed8;
    --blue-900: #1e3a8a;
    --amber-50: #fffbeb;
    --amber-400: #fbbf24;
    --amber-800: #92400e;
}

* { box-sizing: border-box; }

html { -webkit-text-size-adjust: 100%; }

body {
    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text',
                 'Helvetica Neue', 'Segoe UI', 'PingFang TC',
                 'Microsoft JhengHei', sans-serif;
    font-size: 15px;
    line-height: 1.6;
    color: var(--slate-800);
    background: var(--slate-50);
    margin: 0;
    padding: 0;
}

main {
    max-width: 880px;
    margin: 0 auto;
    padding: 48px 56px 64px;
    background: #ffffff;
    box-shadow: 0 1px 3px rgba(15, 23, 42, 0.05),
                0 12px 32px rgba(15, 23, 42, 0.06);
    min-height: 100vh;
}

/* === Top action bar === */
.actions {
    position: sticky;
    top: 0;
    background: rgba(255, 255, 255, 0.92);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    border-bottom: 1px solid var(--slate-200);
    padding: 12px 56px;
    display: flex;
    gap: 12px;
    justify-content: flex-end;
    z-index: 10;
}
.actions a {
    font-size: 13px;
    font-weight: 500;
    color: var(--slate-600);
    text-decoration: none;
    padding: 6px 14px;
    border-radius: 6px;
    border: 1px solid var(--slate-200);
    transition: all 0.15s ease;
}
.actions a:hover {
    color: var(--blue-700);
    border-color: var(--blue-500);
    background: var(--slate-50);
}
.actions a.primary {
    background: var(--blue-700);
    color: #ffffff;
    border-color: var(--blue-700);
}
.actions a.primary:hover {
    background: var(--blue-900);
    border-color: var(--blue-900);
}

/* === H1 / Name === */
h1 {
    font-family: -apple-system, 'SF Pro Display', 'Helvetica Neue',
                 'PingFang TC', sans-serif;
    font-size: 38px;
    font-weight: 700;
    color: var(--slate-900);
    margin: 0 0 4px 0;
    letter-spacing: -0.8px;
}
h1 + p {
    font-size: 17px;
    color: var(--slate-600);
    margin: 0 0 12px 0;
    font-weight: 500;
}
h1 + p + p {
    font-size: 14px;
    color: var(--slate-500);
    margin: 0 0 8px 0;
    line-height: 1.7;
}

/* === H2 / Section heading === */
h2 {
    font-family: -apple-system, 'SF Pro Display', sans-serif;
    font-size: 16px;
    font-weight: 600;
    color: var(--slate-900);
    text-transform: uppercase;
    letter-spacing: 1.2px;
    margin: 36px 0 14px 0;
    padding-bottom: 6px;
    border-bottom: 2px solid var(--blue-500);
}

/* === H3 / Role / Company === */
h3 {
    font-family: -apple-system, 'SF Pro Display', sans-serif;
    font-size: 17px;
    font-weight: 600;
    color: var(--slate-900);
    margin: 24px 0 2px 0;
}
h3 + p {
    margin: 0 0 8px 0;
    font-size: 13.5px;
    color: var(--slate-500);
}
h3 + p em {
    font-style: italic;
}

/* === H4 / Project sub-section === */
h4 {
    font-family: -apple-system, 'SF Pro Display', sans-serif;
    font-size: 14.5px;
    font-weight: 600;
    color: var(--blue-900);
    margin: 18px 0 4px 0;
}
h4 em {
    font-weight: 400;
    font-style: italic;
    color: var(--slate-500);
}

/* === Body === */
p {
    margin: 6px 0;
    line-height: 1.65;
}
p strong {
    color: var(--blue-900);
    font-weight: 600;
}

/* === Bullet lists === */
ul {
    margin: 4px 0 12px 0;
    padding-left: 22px;
    list-style: none;
}
ul li {
    position: relative;
    margin: 4px 0;
    padding-left: 10px;
    line-height: 1.6;
}
ul li::before {
    content: "•";
    color: var(--blue-500);
    font-weight: 700;
    position: absolute;
    left: -4px;
    top: 0;
}

/* === Tables (Skills) === */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0 16px 0;
    font-size: 14px;
}
th, td {
    padding: 8px 12px 8px 0;
    text-align: left;
    vertical-align: top;
    border: none;
    line-height: 1.55;
}
th {
    color: var(--slate-600);
    font-weight: 600;
    border-bottom: 1px solid var(--slate-300);
    padding-bottom: 8px;
}
td:first-child, th:first-child {
    width: 23%;
    color: var(--blue-900);
    font-weight: 600;
    padding-right: 16px;
    white-space: nowrap;
}
tr:not(:last-child) td {
    border-bottom: 1px solid var(--slate-100);
}

/* === HR === */
hr {
    border: 0;
    border-top: 1px solid var(--slate-200);
    margin: 16px 0;
}

/* === Strong === */
strong {
    color: var(--slate-900);
    font-weight: 600;
}

/* === Code === */
code {
    font-family: 'SF Mono', 'Menlo', 'Monaco', 'Consolas', monospace;
    font-size: 13px;
    background: var(--slate-100);
    color: var(--slate-900);
    padding: 1px 5px;
    border-radius: 3px;
}

/* === Links === */
a {
    color: var(--blue-700);
    text-decoration: none;
    border-bottom: 1px solid transparent;
    transition: border-color 0.15s ease;
}
a:hover {
    border-bottom-color: var(--blue-500);
}

/* === Footer === */
footer {
    text-align: center;
    margin-top: 48px;
    padding-top: 24px;
    border-top: 1px solid var(--slate-200);
    font-size: 13px;
    color: var(--slate-500);
}

/* === Responsive === */
@media (max-width: 720px) {
    main { padding: 32px 24px 48px; box-shadow: none; }
    .actions { padding: 10px 20px; }
    h1 { font-size: 30px; }
    h1 + p { font-size: 15px; }
    h2 { font-size: 14px; }
    table, thead, tbody, tr, th, td { display: block; }
    th { display: none; }
    td:first-child {
        width: auto !important;
        white-space: normal;
        padding-top: 12px;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    tr { border-bottom: 1px solid var(--slate-200); padding: 8px 0; }
}

/* === Print: hide actions === */
@media print {
    body { background: #ffffff; }
    main { box-shadow: none; max-width: none; padding: 24px; }
    .actions, footer { display: none; }
}
"""

HTML_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Yu Hsuan Chen (Tina) — Solution Architect / SRE / DevOps</title>
<meta name="description" content="7-year cross-cloud SRE / DevOps engineer. AWS + GCP + on-prem. SOC 2 / ISO 27001. AI-powered SRE tooling.">
<meta property="og:title" content="Yu Hsuan Chen (Tina) — Resume">
<meta property="og:description" content="Solution Architect / SRE / DevOps · 7 yrs cross-cloud">
<meta property="og:type" content="profile">
<style>__CSS__</style>
</head>
<body>
<div class="actions">
  <a href="tina-chen-resume.pdf" class="primary" download>↓ Download PDF</a>
  <a href="https://www.cake.me/resumes/tinachen1996121" target="_blank" rel="noopener">cake.me</a>
</div>
<main>
__BODY__
<footer>
  Last updated: __DATE__ ·
  <a href="tina-chen-resume.pdf" download>PDF version</a>
</footer>
</main>
</body>
</html>
"""


def main() -> None:
    from datetime import date
    md_text = INPUT.read_text(encoding="utf-8")
    html_body = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "nl2br", "sane_lists"],
    )
    html = (
        HTML_HEAD
        .replace("__CSS__", CSS_HTML)
        .replace("__BODY__", html_body)
        .replace("__DATE__", date.today().isoformat())
    )
    OUTPUT.write_text(html, encoding="utf-8")
    print(f"✅ HTML written: {OUTPUT}")
    print(f"   Size: {OUTPUT.stat().st_size / 1024:.1f} KB")


if __name__ == "__main__":
    main()
