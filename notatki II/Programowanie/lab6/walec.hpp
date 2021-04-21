#pragma once
#include "kolo.hpp"

class walec : public kolo {
public:
    int h;
    walec();
    walec(int x, int y, unsigned int r, int h);
    ~walec();
};

