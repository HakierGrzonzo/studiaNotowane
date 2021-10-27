#!/bin/bash
rm -r inputs outputs 2> /dev/null
mkdir inputs
echo "Generuje dane testowe!"
seq 10 20 200 | while read n; do
    ./generate.py $n > inputs/$n.txt
done 
seq 300 100 800 | while read n; do
    ./generate.py $n > inputs/$n.txt
done

mkdir outputs
echo "Zacznynam testy!"
ls ./inputs | while read file; do
    echo "  ###  $file  ###  "
    cat ./inputs/$file | python ./projekt.py | tee ./outputs/out-$file
done

echo "Generuje raport!"
ls inputs | xargs ./raport.py > raport.html
xdg-open raport.html
