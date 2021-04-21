#pragma once
#include "punkt.hpp"

class kolo : public punkt {
public:
    unsigned int r;
    kolo();
    kolo(int x, int y, unsigned int r);
    ~kolo();
};
