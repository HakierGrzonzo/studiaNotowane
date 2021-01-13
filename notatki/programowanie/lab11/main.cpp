#include <fstream>
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

struct Osoba {
    string imie;
    string nazwisko;
    int wiek;
    void display();
};

void Osoba::display()
{
    cout << imie << endl;
    cout << nazwisko << endl;
    cout << wiek << endl;
}

void zapiszOsobe(Osoba o, string nazwaPliku)
{
    ofstream plik;
    plik.open(nazwaPliku);
    if (!plik.is_open())
        throw runtime_error("Plik nie może być read!?");
    plik << o.imie << endl;
    plik << o.nazwisko << endl;
    plik << "wiek: " << o.wiek;
    plik.close();
}

Osoba wczytajOsobe(string nazwaPliku)
{
    ifstream plik;
    plik.open(nazwaPliku);
    if (!plik.is_open())
        throw runtime_error("Plik nie istnieje lub nie może być read");
    string imie;
    getline(plik, imie);
    string nazwisko;
    getline(plik, nazwisko);
    string wiek;
    getline(plik, wiek);
    Osoba o = {imie, nazwisko, stoi(wiek.substr(5))};
    plik.close();
    return o;
}

bool polacz(string plikA, string plikB, string& wynik)
{
    ifstream plikA_p;
    ifstream plikB_p;
    plikA_p.open(plikA);
    plikB_p.open(plikB);
    if (!(plikB_p.is_open() && plikA_p.is_open()))
        return false;
    stringstream res;
    res << plikA_p.rdbuf();
    res << plikB_p.rdbuf();
    wynik = res.str();
    return true;
}

int main(int argc, char** argv)
{
    Osoba o = {"Jan", "Kowalski", 15};
    zapiszOsobe(o, "plswrk.txt");
    Osoba b = wczytajOsobe("plswrk.txt");
    b.display();
}
