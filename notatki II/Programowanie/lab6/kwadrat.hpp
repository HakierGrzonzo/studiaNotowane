#pragma once
#include "punkt.hpp"

class kwadrat {
public:
    punkt wierzchołki[4];
    kwadrat();
    kwadrat(int x1, int x2, int h, int w);
    ~kwadrat();
};
