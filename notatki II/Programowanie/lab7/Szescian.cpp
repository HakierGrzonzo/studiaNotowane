#include "Szescian.hpp"
#include "Kwadrat.hpp"
#include "macro.hpp"

Szescian::Szescian() : Kwadrat() {
    DOM;
}

Szescian::Szescian(float x_) : Kwadrat(x_) {
    PAR;
}

float Szescian::pole() {
    return sqr(x) * 6;
}

Szescian::~Szescian() {
    DES;
}
