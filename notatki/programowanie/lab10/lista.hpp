#pragma once
#include <string>


struct Osoba {
    std::string imie;
    std::string nazwisko;
    int wiek;
    Osoba* kolejna = nullptr;
    void info();
};

struct Lista {
    Osoba* pierwsza = nullptr;
    void info();
    void dodaj(Osoba& osoba);
    void usun(int n);
    void drukujListe();
};
