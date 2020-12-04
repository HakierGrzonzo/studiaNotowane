#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

void statystyka(double* arr, int size)
{
    double* tab = new double[size];
    for (int i = 0; i < size; i++)
    {
        tab[i] = arr[i];
    }
    int swaps;
    do
    {
        swaps = 0;
        for (int i = 1; i < size; i++)
        {
            if (tab[i] < tab[i - 1])
            {
                double tmp = tab[i];
                tab[i] = tab[i - 1];
                tab[i - 1] = tmp;
                swaps++;
            }
        }

    } while (swaps != 0);
    for (int i = 0; i < size; i++)
    {
        cout << tab[i] << endl;
    }
    cout << "Element min: " << tab[0] << endl;
    cout << "Element min: " << tab[size - 1] << endl;
    cout << "Mediana: " << (size % 2 == 0 ? (tab[(size / 2) - 1] + tab[(size / 2)]) / 2 : tab[size/2]);
    delete[] tab;
}
void wypiszSlowa(string slowa[], int size, string phrase)
{
    for (int i = 0; i < size; i++)
    {
        if (slowa[i].find(phrase) != string::npos)
        {
            cout << slowa[i] << endl;
        }
    }

}

int** transpose(int** tab, int sizeX, int sizeY)
{
    int* tabm = new int[sizeX * sizeY];
    for (int i = 0; i < sizeX; i++)
    {
        for (int j = 0; j < sizeY; j++)
        {
            tabm[i * sizeY + j] = tab[i][j];
        }
    }
    int** tab2 = new int*[sizeY];
    for (int i = 0; i < sizeY; i++)
    {
        int* tab3 = new int[sizeX];
        for (int j = 0; j < sizeX; j++)
        {
            tab3[j] = tabm[i + j * sizeY];
        }
        tab2[i] = tab3;
    }
    return tab2;
}

void print(int** tab, int x, int y)
{
    for (int i = 0; i < x; i++)
    {
        for (int j = 0; j < y; j++)
            cout << tab[i][j] << "\t";
        cout << endl;
    }
}

int main()
{
    /*
    cout << "Ile słów potrzebujesz?" << endl;
    int size;
    cin >> size;
    if (size < 2)
    {
        return 1;
    }
    string* liczby = new string[size];
    for (int i = 0; i < size; i++)
    {
        cout << "tab[" << setw(2) << i;
        cout << " ] = ";
        string num;
        cin >> num;
        liczby[i] = num;
    }
    cout << "Szukam frazy '" << liczby[0] << "':" << endl;
    wypiszSlowa(&liczby[1], size - 1, liczby[0]);
    delete[] liczby;
    */
    cout << "Podaj rozmiar tablicy: ";
    int x, y;
    cin >> x >> y;
    if (x < 1 || y < 1) return 1;
    int** tab = new int*[x];
    for (int i = 0; i < x; i++)
    {
        int* tab2 = new int[y];
        for (int j = 0; j < y; j++)
        {
            cin >> tab2[j];
        }
        tab[i] = tab2;
    }
    cout << endl;
    print(tab, x, y);
    cout << endl;
    int** tab3 = transpose(tab, x, y);
    print(tab3, y, x);

}