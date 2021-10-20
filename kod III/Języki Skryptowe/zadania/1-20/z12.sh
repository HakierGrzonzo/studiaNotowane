#!/usr/bin/bash
(IFS=:
for dir in $PATH; do
    echo $dir
    echo "    Liczba plików:" $(ls $dir | wc -l)
    echo ""
done
)
