#include "kolo.hpp"
#include "macro.hpp"

kolo::kolo() : punkt() {
    r = 1;
    print("konstruktor domyślny")
}

kolo::kolo(int x, int y, unsigned int r_) : punkt(x, y) {
    r = r_;
    print("konstruktor parametryczny")
}

kolo::~kolo() {
    print("Destruktor")
}
