#include "punkt.hpp"
#include "macro.hpp"

punkt::punkt() {
    x = 0;
    y = 0;
    print("konstruktor domyślny");
}

punkt::punkt(int x_, int y_) {
    x = x_;
    y = y_;
    print("konstruktor parametryczny");
}

punkt::~punkt() {
    print("Destruktor");
}
