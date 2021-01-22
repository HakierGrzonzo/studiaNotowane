#include <iostream>
#include <string>
#include <fstream>
#include <math.h>
#include <iomanip>

using namespace std;

void wypisz(bool binarnie, int* doWypisania)
{
    for (int i = 0; i < 4; i++)
    {
        if (binarnie)
        {
            int wypisywana = doWypisania[i];
            int tab[8];
            for (int j = 0; j < 8; j++)
            {
                tab[j] = (wypisywana % 2 == 0) ? 0 : 1;
                wypisywana = wypisywana >> 1;
            }
            for (int j = 7; j >= 0; j--)
            {
                cout << tab[j];
            }
            if (i != 3) cout << '.';
        }
        else
        {
            cout << doWypisania[i];
            if (i != 3) cout << '.';
        }
    }
}

struct adresSieciowy 
{
    int* adresIP;
    int* maska;
    void wypiszIP(bool czyBinarnie = true);
    void wypiszMaske(bool czyBinarnie = true);
    void zapiszDoPliku(string nazwaPliku);
};

void adresSieciowy::wypiszIP(bool czyBinarnie)
{
    wypisz(czyBinarnie, adresIP);
    cout << endl;
}

void adresSieciowy::wypiszMaske(bool czyBinarnie)
{
    wypisz(czyBinarnie, maska);
    cout << endl;
}

void adresSieciowy::zapiszDoPliku(string nazwaPliku)
{
    ofstream file;
    file.open(nazwaPliku);
    if (!file.is_open()) throw runtime_error("no");
    file << "IPv4: ";
    for (int i = 0; i < 4; i++)
    {
        file << adresIP[i];
        if (i != 3) file << '.';
    }
    file << endl << "maska: ";
    for (int i = 0; i < 4; i++)
    {
        file << maska[i];
        if (i != 3) file << '.';
    }
    file.close();
}

int main()
{
    adresSieciowy adres {
        new int[4]{192,168,152,113},
        new int[4]{255,255,255,0},
    };
    adres.wypiszMaske();
    adres.wypiszIP(false);
    adres.zapiszDoPliku("test.txt");
}
