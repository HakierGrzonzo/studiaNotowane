#include<iostream>
#include<bitset>
using namespace std;

int len(char text[]){
    int count = 0;
    while (text[count] != '\0') count++;
    return count - 1;
}

int zliczA(char napis[]){
    int res = 0;
    int i = 0;
    while (napis[i] != '\0'){
        if (napis[i] == 'A' || napis[i] == 'a') res++;
        i++;
    }
    return res;
}

void reverse(char napis[]){
    int count = len(napis);
    for (int i = 0; i < count; i++){
        char swap = napis[count];
        napis[count] = napis[i];
        napis[i] = swap;
        count--;
    }
}

double antyprzekatna(double tab[4][4]){
    double res = 1;
    for (int i = 3; i >= 0; i--){
        res *= tab[3 - i][i];
    }
    return res;
}

int main(){
    /*
    char napis[1024];
    cout << "Wprowadź tekst: ";
    cin.getline(napis, 1024);
    cout << zliczA(napis);
    */
    /*
    int n;
    cout << "Podaj liczbę ";
    cin >> n;
    bitset<32> bits(n);
    for (int i = 31; i >= 0; i-- ) {
        cout << bits[i];
        if (i % 8 == 0){
            cout << " ";
        }
    }
    */
    double tab[4][4] {};
    for (int i = 0; i < 4; i++){
        cin >> tab[i][0] >> tab[i][1] >> tab[i][2] >> tab[i][3];
    }
    cout << antyprzekatna(tab);
    return 0;
}