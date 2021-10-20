#!/usr/bin/bash
NOW=$(date +%s)
mkdir wcześniej_niż_trzy_miesiące
ls | while read file; do
    past=$(stat "$file" | grep "Modify: " | awk '{print $2}' | xargs date +%s --date)
    diffrence=$(($NOW-$past))
    days=$(($diffrence/86400))
    if [ "$days" -gt 90 ]; then
        cp -v -r "$file" "wcześniej_niż_trzy_miesiące/"
    else
        echo "Skipping $file"
    fi
done;
