#!/usr/bin/fish

# Skrypt w nie-posix'owej powłoce fish jako ciekawostka, skrypt odtwarza losowo
# pliki muzyki z trackerów (.mod, .it itp) w vlc (bez interfejsu).

# Katalogi z plikami podawane są jako argumenty, przechowywane są jako pliki .zip
# w nestowanych katalogach

mkdir /tmp/modfiles 2> /dev/null
bash -c "rm -r /tmp/modfiles/*" 2> /dev/null
for zipped in (find $argv -iname '*.zip' | shuf)
    # rozpakowywanie pliku
    unzip $zipped -d /tmp/modfiles/ > /dev/null
    # tu się dzieją ciekawe rzeczy, skrypt pozwala skipować piosenki enterem, 
    echo Playing (ls /tmp/modfiles/ | head -n 1 | sed 's/_/ /g')
    # powiadomienie
    notify-send Playing (ls /tmp/modfiles | head -n 1 | sed 's/_/ /g')
    # więc tworzymy 2 procesy w tle
    cvlc --play-and-exit (find /tmp/modfiles | head -n 1) 2> /dev/null &
    bash -c "read" &
    # czekamy aż któryś się zakończy
    wait --any
    # zamykamy ten drugi
    ps | grep -E 'vlc|bash' | awk '{print $1}' | xargs kill
    # czekamy na niedobitki
    wait
    rm -r /tmp/modfiles/*
end
