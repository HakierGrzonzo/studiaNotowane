#!/usr/bin/bash
for extension in  $(ls | rev | sed 's/\./ /' | awk '{print $1}' | rev | sort | uniq | nl| sed 's/\t/:/'); do
    line=$(echo -n $extension | sed 's/:/ /' | awk '{print $1}')
    file=$(echo -n $extension | sed 's/:/ /' | awk '{print $2}')
    file_dump="lista_plikow_$line.txt"
    ls | grep -E "\.$file\$" | sort > $file_dump
done
