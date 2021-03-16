#include "point.hpp"
#include <math.h>

using namespace std;

point::point() {
    x = 0;
    y = 0;
}

point::point(float _x, float _y) {
    x = _x;
    y = _y;
}

float point::distance(point other) {
    return sqrt((x - other.x)  * (x - other.x) + (y - other.y) * (y - other.y));
}
