#include "Kolo.hpp"
#include "macro.hpp"


Kolo::Kolo() {
    DOM;
    r = 0;
}

Kolo::Kolo(float r_) {
    PAR;
    r = r_;
}

float Kolo::pole() {
    return sqr(r) * PI;
}

Kolo::~Kolo() {
    DES;
}
