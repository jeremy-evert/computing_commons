# Build hello.tex and open the resulting PDF on Windows.
# Requires GNU Make, MiKTeX, latexmk, and PowerShell.

DOCUMENT := hello
TEX := $(DOCUMENT).tex
PDF := $(DOCUMENT).pdf
LATEXMK := latexmk
LATEX_FLAGS := -pdf -interaction=nonstopmode -halt-on-error -file-line-error

.PHONY: all build view rebuild clean distclean help

all: build view

build: $(PDF)

$(PDF): $(TEX)
	$(LATEXMK) $(LATEX_FLAGS) $(TEX)

view: $(PDF)
	powershell.exe -NoProfile -Command "Start-Process -FilePath (Resolve-Path '$(PDF)')"

rebuild: clean build view

clean:
	$(LATEXMK) -c $(TEX)

distclean:
	$(LATEXMK) -C $(TEX)

help:
	@echo make          Build hello.pdf when needed, then open a new PDF viewer
	@echo make build    Build hello.pdf without opening it
	@echo make view     Open hello.pdf in a new viewer process
	@echo make rebuild  Clean temporary files, rebuild, and open the PDF
	@echo make clean    Remove temporary LaTeX build files
	@echo make distclean Remove temporary files and hello.pdf
