#!/bin/bash
read -p "Podaj plik: " file
read -p "Podaj max: " max
seq 0 1 $max > $file

