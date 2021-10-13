#!/usr/bin/bash
ls | grep -v "wcześniej_niż_trzy_miesiące" | while read file; do
    diff "$file" "wcześniej_niż_trzy_miesiące/$file"
done;
