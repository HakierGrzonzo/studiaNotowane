#!/bin/bash

# usuwamy autostart według specyfikacji XDG
if [ "$1" == "" ]; then
    rm -i ~/.config/autostart/*
    # Opcje w formacie unixowym, z tego samego powodu co windows
    # ma slashe w inną stronę
elif [ "$1" == "-a" ]; then
    rm  ~/.config/autostart/*
elif [ "$1" == "-h" ]; then
    echo "Usuwa pliki autostartu"
    echo "-a    - usuwa bez pytania"
    echo "-h    - wyświetla tą pomoc"
fi

