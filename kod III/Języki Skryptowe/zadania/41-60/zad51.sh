#!/bin/bash

echo -n "Podaj a: "
read a
echo -n "Podaj b: "
read b

echo "$a + $b = $((a + b))"
echo "$a - $b = $((a - b))"
echo "$a * $b = $((a * b))"
echo "$a / $b = $((a / b))"
