SHELL := /bin/sh
MAIN := main
BUILD := build

.PHONY: all pdf clean watch

all: pdf

pdf:
	powershell -NoProfile -ExecutionPolicy Bypass -File .\build_and_report.ps1 -SkipGit

watch:
	latexmk -pdf -pvc -interaction=nonstopmode -outdir=$(BUILD) $(MAIN).tex

clean:
	latexmk -C -outdir=$(BUILD) $(MAIN).tex
	rm -rf $(BUILD)