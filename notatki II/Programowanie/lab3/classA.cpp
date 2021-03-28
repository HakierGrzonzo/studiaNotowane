#include "classA.hpp"
#include <iostream>
A::A(int num) {
    this->num = num;
    std::cout << "Created object A at " << this << std::endl;
}

void info(A& a)
{
    std::cout << "infoA at " << (void*) info << ": ";
    std::cout << "class A with: " << a.num << " at " << &a.num << std::endl;
}
