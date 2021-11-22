#!/usr/bin/bash

find $1 -iname '*.txt' | while read line; do
    NewName=$(echo $line | rev | cut -c 4- | rev | sed "s/\$/$2/")
    echo $line "->" $NewName
    mv $line $NewName
done;
