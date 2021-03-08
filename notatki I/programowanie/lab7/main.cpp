#include <iostream>
#include <math.h>
using namespace std;


double bisekcja(double(*fun)(double x), double a, double b, double e)
{
    while (true)
    {
        double mid = (a + b) / 2;
        if (abs(b - a) <= 2 * e) return mid;
        if (fun(mid) == 0) return mid;
        if (fun(mid) * fun(a) < 0) b = mid;
        else a = mid;
    }
    return 0;
}

double fun1(double x)
{
    return x*x -9;
}

double fun2(double x)
{
    return sin(x);
}

double fun3(double x)
{
    return x*x*x + 6 * x * x - 144 * x + 256;
}

int main(int argc, char* argv[])
{
    for (int i = 1; i < 4; i++)
    {
        double e = 1 / (pow(10, i));
        cout << "e = " << e << endl;
        cout << bisekcja(fun1, 0, 5, e) << endl;
        cout << bisekcja(fun2, 1, 5, e) << endl;
        cout << bisekcja(fun3, 5, 20, e) << endl;
        cout << endl;
    }
}