#!/bin/bash

echo "Podaj n"
read n
i=0
echo $i > $1
while [ $i -lt $n ]; do
    i=$((i + 1))
    echo $i >> $1
done;
