#include <iostream>
#include "lista.hpp"

int main(int argc, char** argv)
{
    Lista lista {nullptr};
    Osoba jacek {"Jacek", "Wrześniewski", 16};
    Osoba jan {"Jan", "Wrześniewski", 66};
    lista.dodaj(jacek);
    lista.drukujListe();
    std::cout << "---------" << std::endl;
    lista.dodaj(jan);
    lista.drukujListe();
    std::cout << "---------" << std::endl;
    lista.usun(0);
    lista.drukujListe();
    std::cout << "---------" << std::endl;

    return 0;
}