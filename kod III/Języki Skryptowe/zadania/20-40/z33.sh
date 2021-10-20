#!/bin/bash
read -p "Podaj katalog: " dir
echo -e '\033]2;'$dir'\007'
tree $dir
