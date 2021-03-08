#include <string>
#include <iostream>
#include <fstream>

using namespace std;

void wypiszLiczby(int start)
{
    cout << start << ", ";
    if (start > 0)
    {
        wypiszLiczby(start - 5);
        cout << start << ", ";
    }
}

int zmienna;
void trójkąt(int tab[], int size, int sth = 0)
{
    if (size > 0)
    {
        int* nextTab = new int[size - 1];
        for (int i = 0; i < size - 1; i++) nextTab[i] = tab[i] + tab[i + 1];
        trójkąt(nextTab, size - 1);
        for (int i = 0; i < size; i++) cout << tab[i] << (i != size - 1 ? ", " : "\n");
        delete[] nextTab;
    }
}


int main()
{
    //wypiszLiczby(17);
    //cout << "\n----------" << endl;
    //wypiszLiczby(15);
    //int tab[] {0, 1, 2, 3, 4};
    //trójkąt(tab, 5);
    int a = 2, b = 5, c = 3;

    int d = ++a + ++b + c--;
    cout << d << endl;
}
