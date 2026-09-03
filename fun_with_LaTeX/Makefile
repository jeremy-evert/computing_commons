.PHONY: all

all:
	pdflatex -interaction=nonstopmode -halt-on-error -file-line-error hello.tex
	powershell.exe -NoProfile -Command "Start-Process -FilePath (Resolve-Path 'hello.pdf')"
