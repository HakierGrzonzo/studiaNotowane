#include <iostream>
#include "macro.hpp"
#include "punkt.hpp"
#include "kolo.hpp"
#include "walec.hpp"
#include "kwadrat.hpp"
#include "prostopadloscian.hpp"
using namespace std;


int main() {
    cout << "-------- walec domyślny:" << endl;
    walec obj1;
    cout << "-------- prosto- domyślny" << endl;
    prostopaloscian obj2;
    cout << "-------- walec parame" << endl;
    walec obj3(2, 2, 2, 2);
    cout << "-------- prosto- parame" << endl;
    prostopaloscian obj4(5, 5, 5, 5, 5);
    cout << "--------" << endl;
}
