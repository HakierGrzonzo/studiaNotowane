#!/bin/bash
echo "Podaj słowo"
read word
for w in $@; do
    echo $w | sed /$word/d
done
