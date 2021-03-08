#include<cmath>
int euklides(int a, int b){
    int last = 0;
    while(b!= 0)
    {
        last = b;
        b = a % b;
        a = last;
    }
    return a;
}

int sumaCyfr(int n){
    int res = 0;
    while(n != 0)
    {
        res += (n % 10);
        n = n / 10;
    }
    return res;
}

bool czyPierwsza(int n){
    if (n == 1) return false;
    for (int i = 2;  i <= sqrt(n); i++){
        if (n % i == 0){
            return false;
        }
    }
    return true;
}

int potega(int x, int n = 2){
    if (n == 0){
        return 1;
    }
    int res = 1;
    for (int i = 0; i < n; i++) res *= x;
    return res;
}

double potega(double x, int n = 2){
    if (n == 0){
        return 1;
    }
    double res = 1;
    for (int i = 0; i < n; i++) res *= x;
    return res;
}

void potega(int& result, int x, int n = 2){
    result = 1;
    if (n != 0){
        for (int i = 0; i < n; i++) result *= x;
    }
}