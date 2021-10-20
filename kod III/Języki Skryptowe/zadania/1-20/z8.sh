#!/usr/bin/bash
ls "wcześniej_niż_trzy_miesiące" | while read file; do
    echo "----\n$file\n----"
    cat "$file"
done | less;
