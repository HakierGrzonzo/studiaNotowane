#pragma once

template <class T>
class Walec {
    public: 
        Walec(T r, T h);
        T Pole();
    private:
        T r;
        T h;
};
