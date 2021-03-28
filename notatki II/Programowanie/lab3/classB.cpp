#include "classB.hpp"
#include <iostream>

B::B(int num) {
    this->num = new int(num);
    std::cout << "Created object B at " << this << std::endl;
}

void info(B& b)
{
    std::cout << "infoB at " << (void*) info << ": ";
    std::cout << "class B with " << *(b.num) << " at " << b.num << std::endl;
}

B::~B() {
    delete num;
}

B::B(const B& b) {
    std::cout << "Konstruktor kopiujący B" << std::endl;
    this->num = new int(*(b.num));
}
