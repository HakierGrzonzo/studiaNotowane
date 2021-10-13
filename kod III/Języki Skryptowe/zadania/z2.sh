#!/usr/bin/bash
lsblk -o MOUNTPOINTS |\
    awk 'NR!=1' |\
    grep -v '^[[:space:]]*$' |\
    grep -v "\[SWAP\]" |\
    xargs ls
