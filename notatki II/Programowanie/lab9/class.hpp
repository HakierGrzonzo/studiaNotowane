#pragma once
#include "iostream"

class zespolona {
    public:
        zespolona();
        zespolona(double x, double i);
        // jednoargumentowy
        zespolona operator++(int);
        zespolona operator++();
        friend std::ostream& operator<<(std::ostream &ostream, const zespolona& a);
        // dwuargumentowe
        friend zespolona operator+(const zespolona& a, const zespolona&b);
        friend zespolona operator-(const zespolona& a, const zespolona&b);
        bool operator==(const zespolona& other);
        double x;
        double i;
};
std::ostream& operator<<(std::ostream &ostream, const zespolona& a);
zespolona operator+(const zespolona& a, const zespolona&b);
zespolona operator-(const zespolona& a, const zespolona&b);
