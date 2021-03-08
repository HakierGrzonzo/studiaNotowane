#include<iostream>
#include"euklides.h"
using namespace std;


int main(){
    for (int i = 1; i <= 100; i++)
    {
        if (czyPierwsza(i)){
            cout << i << ", ";
        }
        if (i % 20 == 0){
            cout << endl;
        }
    }
}