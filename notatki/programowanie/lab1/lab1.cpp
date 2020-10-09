#include<iostream>
#include<iomanip>
using namespace std;

int main()
{
    /*
    cout << "Podaj a: ";
    float a;
    cin >> a;
    cout << "Podaj b: ";
    float b;
    cin >> b;
    cout << fixed << std::setprecision(3);
    cout << a << " + " << b << " = " << (a + b) << endl;
    cout << a << " - " << b << " = " << (a - b) << endl;
    cout << a << " * " << b << " = " << (a * b) << endl;
    cout << a << " / " << b << " = " << (a / b) << endl;
    cout << "Średnia z " << a << " i " << b << " to " << ((a + b) / 2) << endl;
    */
    /*
    // Linux flex!
    string art = " ╔════╗\n ║żółw║\n ╚════╝\n";
    cout << art;
    // cout << setfill((char) 42) << setw(30) << "Xd" << endl;
    */
    /*
    float xA, xB, yA, yB;
    cout << "Podaj xA: "; 
    cin >> xA;
    cout << "Podaj yA: "; 
    cin >> yA;
    cout << "Podaj xB: "; 
    cin >> xB;
    cout << "Podaj yB: "; 
    cin >> yB;
    float A = (yA - yB) / (xA - xB);
    float B = yA - A*xA;
    if (A == 1)
    {
        cout << "Równanie prostej: y = x + " << B;
    }
    else if (A == -1)
    {
        cout << "Równanie prostej: y = -x + " << B;
    }
    else if (A == 0) {
        cout << "Równanie prostej: y = " << B;
    }
    else if (B < 0) {
        cout << "Równanie prostej: y = " << A << "x - " << -B;
    }
    else
    {
        cout << "Równanie prostej: y = " << A << "x + " << B;
    }
    */
    cout << setfill('*') << setw(10) << "" << endl;

    cout << "Podaj a: ";
    float a;
    cin >> a;
    cout << "Podaj b: ";
    float b;
    cin >> b;
    cout << "Podaj c: ";
    float c;
    cin >> c;

    cout << setw(100) << "" << endl;

    cout << "Podaj x: ";
    float x;
    cin >> x;
    
    cout << setw(100) << "" << endl;

    cout << "f(x) = " << a << "x² + " << b << "x + " << c << endl;
    
    cout << setw(100) << "" << endl;

    cout << "f(" << x << ") = " << (a*x*x + b*x + c) << endl;

    cout << setw(100) << "" << endl;
}