#pragma once
class A {
    public:
        A(int num = 0);
        friend void info(A &a);
    private:
        int num;
};
