#pragma once
#include "Kwadrat.hpp"

class Szescian : public Kwadrat {
    public:
        Szescian();
        Szescian(float x);
        virtual float pole();
        virtual ~Szescian();
};
