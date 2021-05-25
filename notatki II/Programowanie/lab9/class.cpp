#include "class.hpp"
#include <ostream>

zespolona::zespolona() {
    x = 0;
    i = 0;
}

zespolona::zespolona(double x_, double i_) {
    x = x_;
    i = i_;
}

std::ostream& operator<<(std::ostream &ostream, const zespolona& a) {
    ostream << "x = " << a.x << "\ti = " << a.i;
    return ostream;
}

zespolona zespolona::operator++(int) {
    zespolona a = *this;
    x++;
    return a;
}

zespolona zespolona::operator++() {
    x++;
    return *this;
}

zespolona operator+(const zespolona& a, const zespolona& b) {
    return zespolona(a.x + b.x, a.i + b.i);
}

zespolona operator-(const zespolona& a, const zespolona& b) {
    return zespolona(a.x - b.x, a.i - b.i);
}

bool zespolona::operator==(const zespolona& other) {
    return (x == other.x) && (i == other.i);
}

