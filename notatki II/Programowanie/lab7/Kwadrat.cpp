#include "Kwadrat.hpp"
#include "macro.hpp"

Kwadrat::Kwadrat() {
    x = 1;
    DOM;
}

Kwadrat::Kwadrat(float x_) {
    x = x_;
    PAR;
}

float Kwadrat::pole() {
    return sqr(x);
}

Kwadrat::~Kwadrat() {
    DES;
}
