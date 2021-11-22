#!/usr/bin/bash
cat $1 | sed "s/$3/$4/" > $2
