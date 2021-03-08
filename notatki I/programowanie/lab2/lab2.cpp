#include<iostream>
#include<iomanip>
#include<string>
#include<cmath>
using namespace std;

string pp(float num, string suffix, bool addPlus = true, bool sufix = false){
    if (num == 0){
        return "";
    }
    else if (num == 1){
        if (sufix) {
            suffix = "1";
        }
        if (addPlus){
            return " + " + suffix;
        }
        else{
            return suffix;
        }
    }
    else if (num == -1){
        if (sufix) {
            return " - 1";
        }
        return " - " + suffix;
    }
    else if (num > 0) {
        if (addPlus){
            return " + " + to_string(num) + suffix;
        }
        else{
            return to_string(num) + suffix;
        }
    }
    else {
        return " - " + to_string(-num) + suffix;
    }
}

int main()
{
    /*
    cout << setfill('*');

    cout << "Podaj a: ";
    float a;
    cin >> a;
    if (a == 0) {
        cout << "To nie jest funkcja kwadratowa!" << endl;
        return 1;
    }
    cout << "Podaj b: ";
    float b;
    cin >> b;
    cout << "Podaj c: ";
    float c;
    cin >> c;
    cout << endl;
    cout << setw(10) << "" << endl;

    cout << "Funkcja kwadratowa: f(x) = " << pp(a, "x^2", false) << pp(b, "x") << pp(c, "", true, true) << endl;
    
    cout << setw(10) << "" << endl;
    cout << endl;

    float delta = b*b - 4*a*c;
    if (delta < 0){
        cout << "funkcja nie posiada rozwiązań" << endl;
        return 1;
    }
    else if (delta == 0){
        cout << "Funkcja posiada miejsce zerowe x = " << (-b)/(2*a) << endl;
    }
    else {
        cout << "Funkcja posiada dwa miejsca zerowe, x1 = " << (sqrt(delta) - b)/(2*a) << ", x2 = " << (- sqrt(delta) - b)/(2*a) << endl;
    }
    */
    /*int row = 0;
    cout << setw(3) << row << ")";
    for (int i = 0; i < 100; i++){
        if (i % 3 == 0) {
            cout << setw(4) << i;
        }
        if (i % 10 == 0) {
            row++;
            cout << endl << setw(3) << row << ")";
        }
    }
    cout << endl;*/
    cout << "Podaj liczbe: ";
    int max;
    cin >> max;
    for (int i = max; i > 0; i--){
        for (int j = i; j > 0; j--){
            cout << "*";
        }
        cout << endl;
    }
}