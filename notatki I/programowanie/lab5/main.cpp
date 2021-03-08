#include <iostream>
//#include <random>
using namespace std;

void printIntArr(int *arr, int size)
{
    cout << "[";
    for (int i = 0; i < size; i++) cout << arr[i] << ", ";
    cout << "\b\b]" << endl;
}

void generuj_losowe_liczby(int* wsk, int rozmiar, int a, int b)
{
    for (int i = 0; i < rozmiar; i++)
    {
        wsk[i] = (rand() % (b + a + 2)) + a - 1;
    }
}

void pprint(char* string)
{
    int i = 0;
    while (string[i] != '\0')
    {
        if (string[i] != ' ')
        {
            if (string[i] >= 'a' && string[i] <= 'z')
            {
                cout << static_cast<char>  (string[i] - 32);
            }
            else
            {
                cout << string[i];
            }
        }
        i++;
    }
    cout << endl;
}

int max(int* wsk, int size)
{
    int res = wsk[0];
    for(int i = 1; i < size; i++) if (res < wsk[i]) res = wsk[i];
    return res;
}

void kwadraty(int* t1, int* t2, int n)
{
    for (int i = 0; i < n; i++)
    {
        t1[i] = t2[i] * t2[i];
    }
}

int main (int argc, char** argv)
{
    srand (time(NULL));
    int tab2[10] {};
    int tab1[10] {};
    generuj_losowe_liczby(tab2, 10, 0, 10);
    cout  << "tab1: " << std::endl;
    printIntArr(tab1, 10);
    cout  << "tab2: " << std::endl;
    printIntArr(tab2, 10);
    kwadraty(tab1, tab2, 10);
    cout << "Znowu tab1" << endl;
    printIntArr(tab1, 10);
    return 0;
    /*
    cout << "Podaj zdanie: ";
    char zdanie[1024];
    cin.getline(zdanie, 1024);
    pprint(zdanie);
    */
}