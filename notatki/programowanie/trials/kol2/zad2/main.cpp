#include <iostream>
#include <string>
#include <fstream>
#include <math.h>
#include <iomanip>

using namespace std;

double metodaTrapezów(double (*fun)(double), double from, double to, int n)
{
    if (n <= 1 || to <= from ) throw invalid_argument("no");
    double* reses = new double[n];
    int j = 0;
    for (double i = from; i <= to; i += (to - from) / (n - 1))
    {
        reses[j] = fun(i);
        j++;
    }
    double res;
    for (int z = 0; z < n-1; z++)
    {
        res += (reses[z] + reses[z+1]);
    }
    delete[] reses;
    return res*((to - from)/(n - 1)) / 2;
}

double func(double x)
{
    return x*x * cos(x);
}

double testFunc(double x)
{
    return 1;
}
int main()
{
    cout << metodaTrapezów(func, 2, 9, 5);
    cout << endl;
    cout << metodaTrapezów(func, 2, 9, 20);
    cout << endl;
    cout << metodaTrapezów(func, 2, 9, 100);
    cout << endl;
}
