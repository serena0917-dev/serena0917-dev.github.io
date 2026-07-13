# yh chen — Resume

Source of truth for my resume, deployed at **https://serena0917-dev.github.io/**.

## Files

| File | What |
|---|---|
| `tina-chen-resume.md` | Markdown source (edit this) |
| `index.html` | Rendered HTML (generated, deployed to Pages) |
| `tina-chen-resume.pdf` | Styled PDF (generated, download from Pages) |
| `build_resume_html.py` | Markdown → HTML (Stripe/Linear style) |
| `build_resume_pdf.py` | Markdown → PDF (WeasyPrint) |

## Update workflow

```bash
# 1. Edit the markdown
$EDITOR tina-chen-resume.md

# 2. Regenerate HTML + PDF
uv run --with markdown build_resume_html.py
uv run --with weasyprint --with markdown build_resume_pdf.py

# 3. Commit + push (Pages auto-deploys in ~30s)
git add -A && git commit -m "update resume" && git push
```

## Stack

- **Content**: Markdown
- **HTML rendering**: Python `markdown` + custom CSS (system font stack, Stripe/Linear visual style)
- **PDF rendering**: WeasyPrint (CSS Paged Media, no headless browser)
- **Hosting**: GitHub Pages (user pages, served from `main` branch root)
- **Cache busting**: Not needed — Pages CDN respects file mtime
