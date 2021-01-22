#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>
#include <vector>

using namespace std;

int main()
{
    ifstream dane;
    dane.open("kod.txt");
    if (!dane.is_open()) throw runtime_error("no");
    vector<string> odczytane; // Co nie jest zabronione jest dozwolone
    string buffer;
    while (!dane.eof())
    {
        char in;
        dane.get(in);
        if (in == '0') buffer += "0";
        else if (in == '1') buffer += "1";
        else if (in == ' ')
        {
            odczytane.push_back(buffer);
            buffer = "";
        }
    }
    if (buffer.size() > 0) odczytane.push_back(buffer);
    string* tablica = new string[odczytane.size()];
    /*
     * vector ma pewnie metode do tego ale nie chce mi się jej szukać
     * pozatym trzeba zrobić to `dynamicznie`
     */
    for (int i = 0; i < odczytane.size(); i++)
    {
        tablica[i] = odczytane[i];
    }
    unsigned int* nums = new unsigned int[odczytane.size()];
    for (int i = 0; i < odczytane.size(); i++)
    {
        int temp = 0;
        int potega = 1;
        for (int z = tablica[i].size() - 1; z >= 0; z--)
        {
            if (tablica[i][z] == '1') temp += potega;
            potega *= 2;
        }
        nums[i] = temp;
    }
    for (int i = 0; i < odczytane.size(); i++)
    {
        cout << (char) nums[i];
    }
    cout << endl;
    delete[] nums;
    delete[] tablica;
}
