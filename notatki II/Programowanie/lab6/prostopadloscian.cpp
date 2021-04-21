#include "prostopadloscian.hpp"
#include "kwadrat.hpp"
#include "macro.hpp"

prostopaloscian::prostopaloscian() : kwadrat() {
    print("konstruktor domyślny");
    h = 1;
}

prostopaloscian::prostopaloscian(int x1, int x2, int h, int w, int hp) : kwadrat(x1, x2, h, w){
    print("konstruktor parametryczny");
    h = hp;
}

prostopaloscian::~prostopaloscian() {
    print("destruktor");
}

