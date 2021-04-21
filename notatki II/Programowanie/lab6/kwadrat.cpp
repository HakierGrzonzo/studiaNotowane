#include "kwadrat.hpp"
#include "punkt.hpp"
#include "macro.hpp"

kwadrat::kwadrat() {
    print("Konstruktor domyślny");
    wierzchołki[0] = punkt(0, 0);
    wierzchołki[1] = punkt(1, 0);
    wierzchołki[2] = punkt(1, 1);
    wierzchołki[3] = punkt(0, 1);
}

kwadrat::kwadrat(int x1, int x2, int h, int w) {
    print("Konstruktor parametryczny");
    wierzchołki[0] = punkt(x1, x2);
    wierzchołki[1] = punkt(x1 + h, x2);
    wierzchołki[2] = punkt(x1 + h, x2 + w);
    wierzchołki[3] = punkt(x1, x2 + w);
}

kwadrat::~kwadrat() {
    print("destruktor");
}
