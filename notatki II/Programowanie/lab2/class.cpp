#include "class.hpp"
#include <iostream>

Cosiek::Cosiek(int _number) {
    numerek = new int(_number);
}

Cosiek::Cosiek(const Cosiek &org) {
    numerek = new int(*org.numerek);
}

Cosiek::~Cosiek() {
    delete numerek;
}

void Cosiek::info() {
    std::cout << "Mam konstruktor kopiujący i numerek " << numerek << std::endl;
}
