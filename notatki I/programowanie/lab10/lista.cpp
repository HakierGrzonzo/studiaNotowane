#include <string>
#include <iostream>

struct Osoba {
    std::string imie;
    std::string nazwisko;
    int wiek;
    Osoba* kolejna = nullptr;
    void info();
    void dodaj(Osoba& osoba);
    void usun(int n);
};

struct Lista {
    Osoba* pierwsza = nullptr;
    void info();
    void dodaj(Osoba& osoba);
    void usun(int n);
    void drukujListe();
};

void Osoba::dodaj(Osoba& osoba)
{
    if (kolejna == nullptr)
    {
        kolejna = &osoba;
    }
    else
    {
        kolejna->dodaj(osoba);
    }
}

void Osoba::info()
{
    std::cout << imie << " " << nazwisko << " Wiek:" << wiek << std::endl;
}

void Lista::dodaj(Osoba& osoba)
{
    if(pierwsza == nullptr)
    {
        pierwsza = &osoba;
    }
    else
    {
        pierwsza->dodaj(osoba);
    }
}

void Lista::usun(int n)
{
    if (n == 0)
    {
        pierwsza = pierwsza->kolejna;
    }
    else
    {
        pierwsza->usun(n);
    }
}

void Osoba::usun(int n)
{
    if (n == 1)
    {
        kolejna = kolejna->kolejna;
    }
    else
    {
        kolejna->usun(--n);
    }
}

void Lista::drukujListe()
{
    Osoba* osoba_ = pierwsza;
    while (osoba_ != nullptr)
    {
        osoba_->info();
        osoba_ = osoba_->kolejna;
    }
}