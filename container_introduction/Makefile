SHELL := /bin/sh
MAIN := main
BUILD := build

.PHONY: all pdf clean watch

all: pdf

pdf:
	mkdir -p $(BUILD)
	latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=$(BUILD) $(MAIN).tex

watch:
	latexmk -pdf -pvc -interaction=nonstopmode -outdir=$(BUILD) $(MAIN).tex

clean:
	latexmk -C -outdir=$(BUILD) $(MAIN).tex
	rm -rf $(BUILD)