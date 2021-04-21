#pragma once
#include "kwadrat.hpp"

class prostopaloscian : public kwadrat {
public:
    int h;
    prostopaloscian();
    prostopaloscian(int x1, int x2, int h, int w, int hp);
    ~prostopaloscian();
};
