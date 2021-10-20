#!/bin/bash
# skrypt wymaga imagemagick

ls *.png *.jpg | while read file; do
    convert "$file" "$file.eps"
done;
