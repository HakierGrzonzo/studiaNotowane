#pragma once
#include "obiekt.hpp"

class Kolo : public Object {
    public:
        Kolo();
        Kolo(float r);
        virtual float pole();
        virtual ~Kolo();
    protected:
        float r;
};

