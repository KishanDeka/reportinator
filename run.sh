#!/bin/bash
cd _scripts/
rm ../tex_out/*
python main.py > ../tex_out/report.tex
cd ../tex_out
pdflatex report.tex
