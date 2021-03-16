#pragma once
#include "point.hpp"

class circle {
    public:
        circle();
        circle(point _center, float _radius);
        bool isInCircle(point other);
    private:
        float radius;
        point center;
};
