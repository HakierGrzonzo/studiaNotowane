#!/usr/bin/bash
read type
rm "*.$type" 2> /dev/null || echo "Nie znaleziono plków .$type"
