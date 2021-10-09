#!/usr/bin/bash
echo "Compering $(ls | head -n 2 | xargs echo)"
ls | head -n 2 | xargs diff
