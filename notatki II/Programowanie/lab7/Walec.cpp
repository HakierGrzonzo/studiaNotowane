#include "Walec.hpp"
#include "Kolo.hpp"
#include "macro.hpp"


Walec::Walec() : Kolo() {
    DOM;
    h = 0;
}

Walec::Walec(float r_, float h_) : Kolo(r_) {
    PAR;
    h = h_;
}

float Walec::pole() {
    return sqr(r) * PI * h;
}

Walec::~Walec() {
    DES;
}
