#!/bin/bash
pandoc --slide-level 2 --pdf-engine xelatex -t beamer -V handout prezka.md -o prezka-full.pdf
