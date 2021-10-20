#!/bin/bash
read -p "Podaj katalog: " dir
echo -e '\033]2;'$dir'\007'
read -p "Podaj plik docelowy: " file
ls $dir | tee $file > /dev/null
