#!/usr/bin/bash
cat $1
echo "----"
cat $1 | sed "s/$2/$3/"
