#include <string>
#include <iostream>
#include <fstream>
#include "class.hpp"
#include "classNoCopy.hpp"

using namespace std;

int main()
{
    cout << "Klasy z konstuktorem kopiującym" << endl;
    Cosiek a = Cosiek();
    Cosiek b = a;
    a.info();
    b.info();
    cout << "Zwiększamy w jednej o jeden" << endl;
    a.numerek[0]++;
    a.info();
    b.info();
    cout << endl;
    // bez konstruktora kopiującego
    cout << "Klasy bez konstruktora kopiującego" << endl;
    Cosiek2 a2 = Cosiek2(420);
    Cosiek2 b2 = a2;
    a2.info();
    b2.info();
    cout << "Zwiększamy w jednej o jeden" << endl;
    a2.numerek[0]++;
    a2.info();
    b2.info();
}
