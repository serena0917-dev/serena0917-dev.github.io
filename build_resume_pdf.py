#!/usr/bin/env python3
"""
Resume Markdown → PDF (Stripe / Linear-inspired styling)

Usage:
    uv run --with weasyprint --with markdown build_resume_pdf.py

Renders ~/Documents/resume/tina-chen-resume.md to tina-chen-resume.pdf
with modern minimal tech-company resume styling.
"""

from pathlib import Path
import markdown
from weasyprint import CSS, HTML

INPUT = Path(__file__).parent / "tina-chen-resume.md"
OUTPUT = Path(__file__).parent / "tina-chen-resume.pdf"

# Stripe / Linear-style resume CSS
CSS_RESUME = """
@page {
    size: A4;
    margin: 1.6cm 1.8cm 1.6cm 1.8cm;
}

* { box-sizing: border-box; }

body {
    font-family: -apple-system, 'SF Pro Text', 'Helvetica Neue',
                 'PingFang TC', 'Microsoft JhengHei', sans-serif;
    font-size: 9.5pt;
    line-height: 1.55;
    color: #1f2937;            /* slate-800 */
    margin: 0;
}

/* === Profile photo === */
.profile-photo {
    float: right;
    width: 100pt;
    height: auto;
    margin: 0 0 8pt 14pt;
    border-radius: 4pt;
    object-fit: cover;
}

/* === Name (H1) === */
h1 {
    font-family: -apple-system, 'SF Pro Display', 'Helvetica Neue',
                 'PingFang TC', sans-serif;
    font-size: 26pt;
    font-weight: 700;
    color: #0f172a;            /* slate-900 */
    margin: 0 0 2pt 0;
    letter-spacing: -0.5pt;
}

/* === Job-title subtitle (first strong after H1) === */
h1 + p strong {
    font-weight: 500;
    font-size: 12pt;
    color: #475569;            /* slate-600 */
}
h1 + p {
    margin: 0 0 6pt 0;
    font-size: 12pt;
    color: #475569;
}

/* === Contact line === */
h1 + p + p {
    font-size: 9pt;
    color: #64748b;            /* slate-500 */
    margin: 0 0 4pt 0;
    line-height: 1.5;
}

/* === Section heading (H2) === */
h2 {
    font-family: -apple-system, 'SF Pro Display', 'Helvetica Neue',
                 'PingFang TC', sans-serif;
    font-size: 11.5pt;
    font-weight: 600;
    color: #0f172a;
    text-transform: uppercase;
    letter-spacing: 0.8pt;
    margin: 16pt 0 6pt 0;
    padding-bottom: 3pt;
    border-bottom: 1.5pt solid #3b82f6;   /* blue-500 accent */
}

/* === Sub-section (H3) — role / company line === */
h3 {
    font-family: -apple-system, 'SF Pro Display', sans-serif;
    font-size: 10.5pt;
    font-weight: 600;
    color: #0f172a;
    margin: 8pt 0 1pt 0;
}

/* === Date / location italics under H3 === */
h3 + p em {
    color: #64748b;
    font-size: 9pt;
    font-style: italic;
}
h3 + p {
    margin: 0 0 4pt 0;
}

/* === Body paragraphs === */
p {
    margin: 3pt 0;
}

/* === Bold sub-cluster headers in experience (☁️ / ⎈ / etc.) === */
p strong {
    color: #1e3a8a;            /* blue-900 */
    font-weight: 600;
    font-size: 9.8pt;
}

/* === Bullet lists === */
ul {
    margin: 2pt 0 6pt 0;
    padding-left: 14pt;
    list-style: none;
}
ul li {
    position: relative;
    margin: 2pt 0;
    padding-left: 8pt;
    line-height: 1.5;
}
ul li::before {
    content: "•";
    color: #3b82f6;            /* blue accent dot */
    font-weight: 700;
    position: absolute;
    left: -2pt;
    top: 0;
}

/* === Nested level-2 lists (rare) === */
ul ul li::before { color: #94a3b8; }

/* === Highlights / Profile bullets — slightly stronger === */
h2 + ul li, h2 + p + ul li {
    line-height: 1.5;
}

/* === Tables (Skills section) === */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 4pt 0 6pt 0;
    font-size: 9pt;
}
th, td {
    padding: 4pt 8pt 4pt 0;
    text-align: left;
    vertical-align: top;
    border: none;
}
th {
    color: #475569;
    font-weight: 600;
    border-bottom: 0.5pt solid #cbd5e1;
    padding-bottom: 4pt;
}
td:first-child, th:first-child {
    width: 22%;
    color: #1e3a8a;
    font-weight: 600;
    padding-right: 12pt;
}
tr:not(:last-child) td {
    border-bottom: 0.5pt solid #f1f5f9;
}

/* === Horizontal rule === */
hr {
    border: 0;
    border-top: 0.5pt solid #e2e8f0;
    margin: 8pt 0;
}

/* === Blockquote (placeholder hints) === */
blockquote {
    margin: 4pt 0;
    padding: 4pt 8pt;
    border-left: 2pt solid #fbbf24;   /* amber accent for placeholders */
    background: #fffbeb;              /* amber-50 */
    color: #92400e;                   /* amber-800 */
    font-size: 8.5pt;
    font-style: italic;
}

/* === Inline code (skill names, repos) === */
code {
    font-family: 'SF Mono', 'Menlo', 'Monaco', monospace;
    font-size: 8.8pt;
    background: #f1f5f9;
    color: #0f172a;
    padding: 0.5pt 3pt;
    border-radius: 2pt;
}

/* === Strong emphasis (numbers / scope) === */
strong {
    color: #0f172a;
    font-weight: 600;
}

/* === Em (subtitle italics) === */
em {
    color: #475569;
}
"""


def main() -> None:
    md_text = INPUT.read_text(encoding="utf-8")
    html_body = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "nl2br", "sane_lists"],
    )
    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><title>Resume</title></head>
<body>{html_body}</body>
</html>"""

    HTML(string=html_doc).write_pdf(
        target=str(OUTPUT),
        stylesheets=[CSS(string=CSS_RESUME)],
    )
    print(f"✅ PDF written: {OUTPUT}")
    print(f"   Size: {OUTPUT.stat().st_size / 1024:.1f} KB")


if __name__ == "__main__":
    main()
