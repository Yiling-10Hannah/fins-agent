# Legacy LaTeX Setup Guide

LaTeX is **optional** and no longer part of first-time onboarding. The default
course writing path is Word through `report/report.docx`.

Use this guide only when you explicitly need to compile a legacy `.tex` report
or Beamer deck. All Python work and the default Word report workflow function
without LaTeX.

## Windows - MiKTeX

MiKTeX auto-installs missing LaTeX packages when you compile a document.

**Install**:
```
winget install MiKTeX.MiKTeX
```

Or download from: https://miktex.org/download

**Configure** (important!):
1. Open **MiKTeX Console** (search in Start menu)
2. Go to **Settings**
3. Set "Install missing packages on the fly" to **Yes**

**Verify**:
```
pdflatex --version
```

## macOS - BasicTeX

BasicTeX is a lightweight LaTeX distribution (~100MB) that works natively
on Apple Silicon Macs.

**Install**:
```bash
brew install --cask basictex
```

**Close and reopen Terminal**, then install common packages:
```bash
sudo tlmgr update --self
sudo tlmgr install collection-latexrecommended
```

**Verify**:
```bash
pdflatex --version
```

**If you need additional packages later**:
```bash
sudo tlmgr install package-name
```

## Compiling a LaTeX Document

```bash
pdflatex my_paper.tex
bibtex my_paper
pdflatex my_paper.tex
pdflatex my_paper.tex
```

Yes, you run `pdflatex` multiple times - this resolves cross-references
and citations. Your AI coding assistant can handle this for you.
