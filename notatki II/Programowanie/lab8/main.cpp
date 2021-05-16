#include <iostream>
#include "macro.hpp"
#include "class.hpp"

using namespace std;

template <class T> Walec<T>::Walec(T r_, T h_) {
    r = r_;
    h = h_;
}
template <class T> T Walec<T>::Pole() {
    return 2 * PI * sqr(r) + PI * r * 2 * h;
}

template <typename T>
T max(const T x, const T y, const T z) {
    return max(x, max(y, z));
}

int main() {
    printName(max(5, 10));
    printName(max(PI, 2.137, -1.0));
    // typy mające sens
    printName(Walec<float>(2.13769420, 70000000).Pole())
    printName(Walec<double>(2.13769420, 70000000).Pole())
    // typy mające średni sens
    printName(Walec<int>(2.13769420, 70000000).Pole())
    printName(Walec<unsigned long long>(2.13769420, 70000000).Pole())
    // Standard określa to jako `undefined behaviour` więc 
    // inny kompilator niż g++ 10.2.0 pewnie da co innego, 
    // włącznie z wybuchem komputera czy czymkolwiek innym.
    // Zatem załączam swoje wyniki:
    printName(Walec<char>(2.13769420, 70000000).Pole()) // wypisuje <80>
    printName(Walec<bool>(2.13769420, 70000000).Pole()) // wypisuje 1
}
