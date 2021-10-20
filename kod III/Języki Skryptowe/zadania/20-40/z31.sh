#/bin/bash
read -p "Podaj imię: " name
echo -e '\033]2;'$name'\007'
echo "Niektóre powłoki nadpisują tytuł okna"
sleep 5
