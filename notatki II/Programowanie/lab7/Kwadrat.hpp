#pragma once
#include "obiekt.hpp"

class Kwadrat : public Object {
    public:
        Kwadrat();
        Kwadrat(float x);
        virtual float pole();
        virtual ~Kwadrat();
    protected:
        float x;
};
