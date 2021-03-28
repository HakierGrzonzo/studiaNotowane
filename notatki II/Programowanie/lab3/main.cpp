#include <iostream>
#include "classA.hpp"
#include "classB.hpp"
using namespace std;

int main()
{
    cout << "konstruktor kopiujący domyślny" << endl;
    A a;
    info(a);
    A a1 = a;
    info(a1);
    cout << endl;
    cout << "Z konstruktorem kopiującym" << endl;
    cout << endl;
    B b;
    info(b);
    B b1 = b;
    info(b1);
    // Kopiuje się funkcja zaprzyjaźniona ale jej adres pozostaje taki sam.
    // Nie wymaga
    // Nie, uruchamiany jest konstruktor kopiujący (jak jego nie ma to kompilator go tworzy)
}
