#include "circle.hpp"
#include "point.hpp"
#include <stdexcept>

using namespace std;

circle::circle() {
    center = point();
    radius = 1;
}

circle::circle(point _center, float _radius) {
    if (_radius  <= 0) {
        throw new invalid_argument("radius is not positive");
    }
    center = _center;
    radius = _radius;
}

bool circle::isInCircle(point other) {
    return center.distance(other) <= radius;
}
