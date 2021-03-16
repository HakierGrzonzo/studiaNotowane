#include <stdexcept>
#include <string>
#include <iostream>
#include <fstream>
#include "circle.hpp"
#include "point.hpp"
using namespace std;

int main()
{
    cout << "Podaj x koła: ";
    float x;
    cin >> x;
    cout << "Podaj y koła: ";
    float y;
    cin >> y;
    cout << "Podaj średnice koła: ";
    float r;
    cin >> r;
    try {
        circle roundOne = circle(point(x, y), r);
        cout << "Podaj x koła: ";
        cin >> x;
        cout << "Podaj y koła: ";
        cin >> y;
        if (roundOne.isInCircle(point(x, y))) {
            cout << "Punkt jest w kole" << endl;
        }
        else {
            cout << "Punkt nie jest w kole" << endl;
        }
    } catch (...) {
        cerr << "Średnica musi być dodatnia" << endl;
        return 1;
    }
}
