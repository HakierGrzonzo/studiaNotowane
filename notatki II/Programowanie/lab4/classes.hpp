#pragma once

#define metoda public

class A {
    public:
        int apub;
    metoda:
        void metodaA();
    protected:
        int aprot;
    private:
        int apriv;
};

class B : private A {
    public:
        int bpub;
    metoda:
        void metodaB();
    protected:
        int bprot;
    private:
        int bpriv;
};

class C : private B {
    public:
        int cpub;
    metoda:
        void metodaC();
    protected:
        int cprot;
    private:
        int cpriv;
};
