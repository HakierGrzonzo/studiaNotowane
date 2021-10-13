#!/usr/bin/bash
cat /etc/hostname
echo "Liczba woluminów:" $(lsblk -o LABEL | awk 'NR!=1' | wc -l) 
echo "Nazwy:"
lsblk -o NAME,LABEL -l | awk 'NR!=1' 
echo "Liczba interfejsów sieciowych:" $(ls /sys/class/net | wc -l)
echo "Adresy MAC:"
ls /sys/class/net | while read interface; do
    cat /sys/class/net/$interface/address
done;

