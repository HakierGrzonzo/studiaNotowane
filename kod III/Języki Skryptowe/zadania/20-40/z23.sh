#!/usr/bin/bash
cat jakies_pliki.txt | while read file; do
   cat $1 | ./$file | tee $2
done
