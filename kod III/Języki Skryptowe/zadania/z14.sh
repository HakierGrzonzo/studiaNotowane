#!/usr/bin/bash
echo "Mamy" $(ps aux | awk 'NR!=1' | wc -l) "procesów"
