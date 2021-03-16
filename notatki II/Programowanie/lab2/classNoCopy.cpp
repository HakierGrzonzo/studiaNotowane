#include "classNoCopy.hpp"
#include <iostream>

Cosiek2::Cosiek2(int _number) {
    numerek = new int(_number);
}

Cosiek2::~Cosiek2() {
    //free() nie lubi podwójnych delete dla jednego pointera
    //delete numerek; 
}

void Cosiek2::info() {
    std::cout << "Mam numerek " << numerek << " i nie mam konstruktora kopiującego" << std::endl;
}
