#!/bin/bash

echo -n "Naciśnij y by kontynuować "
read key
if [ $key == "y" ]; then
    echo "done"
else
    exit 1
fi

