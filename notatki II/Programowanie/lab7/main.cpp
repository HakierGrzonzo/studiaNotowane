#include <iostream>
#include "Walec.hpp"
#include "macro.hpp"
#include "Kwadrat.hpp"
#include "Kolo.hpp"
#include "obiekt.hpp"
#include "Szescian.hpp"

using namespace std;

void printFunc(Object* obj) {
    printName(obj->pole());
}

int main() {
    Kwadrat kwadrat(10);
    printName(kwadrat.pole());
    printFunc(&kwadrat);
    cout << "-------" << endl;
    Kolo kolo(5);
    printName(kolo.pole());
    printFunc(&kolo);
    cout << "-------" << endl;
    Walec walec(5, 10);
    printName(walec.pole());
    printFunc(&walec);
    cout << "-------" << endl;
    Szescian szescian(10);
    printName(szescian.pole());
    printFunc(&szescian);
    cout << "-------" << endl;
}
