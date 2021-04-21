#include <iostream>
#include <string>

using namespace std;

string makeRow(int len, int max) {
    string res;
    len = len - 1;
    for (int i = 0; i < max - len; i++) res += " ";
    for (int i = 0; i < len; i++) res += "*";
    res += "*";
    for (int i = 0; i < len; i++) res += "*";
    return res;
}

int main(int argc, char** argv) {
    int rozmiar = 0;
    if (argc == 2) {
        rozmiar = atoi(argv[1]);
    }
    else {
        cout << "Podaj rozmiar bloku pierwszego: ";
        cin >> rozmiar;
    }
    if (rozmiar < 2) {
        cerr << "Za mały rozmiar" << endl;
        return 1;
    }
    else {
        int maxRozmiar = rozmiar * 3 - 2;
        for (int i = 1; i < rozmiar + 1; i++) cout << makeRow(i, maxRozmiar) << endl;
        int nowyMin = rozmiar - 1;
        int nowyMax = nowyMin + rozmiar + 2;
        for (int i = nowyMin; i < nowyMax; i++) cout << makeRow(i, maxRozmiar) << endl;
        nowyMin = nowyMax - 4;
        nowyMax = nowyMin + rozmiar + 2;
        for (int i = nowyMin; i < nowyMax; i++) cout << makeRow(i, maxRozmiar) << endl;
        for (int i = 0; i < rozmiar; i++) cout << makeRow(1, maxRozmiar) << endl;
    }
}
