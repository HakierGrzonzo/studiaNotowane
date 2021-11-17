#!/bin/bash
echo "Podaj słowo"
read word
for w in cat $1; do
    echo $w | sed /$word/d
done
