#!/bin/bash
ls $1/*.jpg $1/*.png | while read file; do
    convert "$file" "$file.eps"
done;
ls $1/*.jpg $1/*.png $1/*.eps > tabela 2> /dev/null
