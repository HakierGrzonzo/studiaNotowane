#pragma once
#include "Kolo.hpp"

class Walec : public Kolo {
    public:
        Walec();
        Walec(float r, float h);
        virtual float pole();
        virtual ~Walec();
    private:
        float h;
};

