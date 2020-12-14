#include <iostream>
#include <string>

enum Platforma {
    PS4,
    PS5,
    Xbox,
    Switch,
    PC
};

struct Gra
{
    std::string tytul;
    std::string wydawca;
    unsigned int rokWydania;
    Platforma platforma;
    int cena;
    void info()
    {
        std::cout << "Title:\t" << tytul << std::endl <<
            "Wydawca:\t" << wydawca << std::endl <<
            "rokWydania:\t" << rokWydania << std::endl << "Platforma:\t";
        std::string names[] = {"PS4", "PS5", "Xbox", "Switch", "PC"};
        std::cout << names[static_cast<int>(platforma)] << std::endl << "Cena:\t" << cena << std::endl;
    };
};

struct KolekcjaGier {
    Gra* kolekcja;
    int size;
    void wypiszGre(int n)
    {
        if (n < size) kolekcja[n].info();
    }
    void wypiszWszystkie()
    {
        for (int i = 0; i < size; i++)
        {
            wypiszGre(i);
        }
    }
    Gra searchByTitle(std::string title)
    {
        for (int i = 0; i < size; i++)
        {
            if (kolekcja[i].tytul == title) return kolekcja[i];
        }
        return Gra {};
    }
    void wypiszPoPlatformie(Platforma p)
    {
        for (int i = 0; i < size; i++)
        {
            if (kolekcja[i].platforma == p) kolekcja[i].info();
        }
    }
    void wypiszPoCenieFancy()
    {
        int swaps;
        do
        {
            swaps = 0;
            for (int i = 1; i < size; i++)
            {
                if (kolekcja[i].cena < kolekcja[i - 1].cena)
                {
                    Gra tmp = kolekcja[i];
                    kolekcja[i] = kolekcja[i - 1];
                    kolekcja[i - 1] = tmp;
                    swaps++;
                }
            }
        } while (swaps != 0);
        wypiszWszystkie();
    }
};

void line()
{
    std::cout << std::endl << "------" << std::endl;
}

void binary(unsigned int a)
{
    for (int i = 0; i < sizeof(unsigned int) * 8; i++)
    {
        if (a % 2 == 1) std::cout << '1';
        else std::cout << '0';
        a = a >> 1;
    }
}

int ile_bitów_różnicy(unsigned int a, unsigned int b)
{
    unsigned int mask = 0b1;
    unsigned int c = (a ^ b);
    int res = 0;
    for (int i = 0; i < sizeof(unsigned int) * 8; i++)
    {
        if ((c & mask) > 0)
        {
            res++;
        }
        c = c >> 1;
    }
    return res;
}


int main()
{
    Gra gra1 = {"Cajberbunk 1977", "DVDproject", 2019, Platforma::PC, 15};
    Gra gra2 = {"Cajberbunk 1975", "DVDproject", 2019, Platforma::PS4, 20};
    Gra gra3 = {"Cajberbunk 1976", "DVDproject", 2019, Platforma::PC, 150};
    Gra gry[] = {gra1, gra2, gra3};
    KolekcjaGier kolekcjaGier = {gry, 3};
    kolekcjaGier.wypiszWszystkie();
    line();
    kolekcjaGier.wypiszGre(1);
    line();
    kolekcjaGier.wypiszPoPlatformie(Platforma::PS4);
    line();
    kolekcjaGier.wypiszPoCenieFancy();
}