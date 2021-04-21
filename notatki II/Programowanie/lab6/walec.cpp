#include "walec.hpp"
#include "macro.hpp"

walec::walec() : kolo() {
    h = 1;
    print("konstruktor domyślny")
}

walec::walec(int x, int y, unsigned int r, int h_) : kolo(x, y, r) {
    h = h_;
    print("konstruktor parametryczny")
}

walec::~walec() {
    print("Destruktor")
}
