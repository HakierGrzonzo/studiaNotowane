#pragma once
class B {
    public:
        B(int num = 0);
        friend void info(B &b);
        B(const B &b);
        ~B();
    private:
        int* num;
};
