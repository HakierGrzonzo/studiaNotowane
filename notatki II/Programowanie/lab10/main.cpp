#include "macro.hpp"
#include <string>

using namespace std;

int Dziel(int a, int b) {
    if (b == 0) {
        throw string("Dzielenie przez zero!");
    }
    return a / b;
}

int modulo(int a, int b) {
    if (b == 0) {
        throw string("B jest równe zero!");
    }
    if (a == b) {
        throw string("A jest równe B");
    }
    if (a == 0) {
        return a;
    }
    while(a >= b) {
        a -= b;
    }
    if (a == 0) {
        throw string("B jest wielokrotnością A");
    }
    return a;
}

int main() {
    cout << "Podaj a: ";
    int a;
    cin >> a;
    cout << "Podaj b: ";
    int b;
    cin >> b;
    try {
        int res = Dziel(a, b);
        cout << "Dzielenie a/b = " << res << endl;
    } catch (string stuff) {
        cout << stuff << endl;
    }
    try {
        int res = modulo(a, b);
        cout << "a % b = " << res << endl;
    } catch (string stuff) {
        cout << stuff << endl;
    }
}
