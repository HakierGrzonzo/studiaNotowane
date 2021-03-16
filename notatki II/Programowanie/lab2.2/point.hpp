#pragma once

class point {
    public:
        float x, y;
        point();
        point(float x, float y);
        float distance (point other);
};
