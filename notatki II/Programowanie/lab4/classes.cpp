#include "classes.hpp"

void A::metodaA() {
    metodaA();
    apub = 0;
    aprot = 0;
    apriv = 0;
}

void B::metodaB() {
    metodaA();
    apub = 0;
    aprot = 0;
    apriv = 0;

    metodaB();
    bpub = 0;
    bprot = 0;
    bpriv = 0;
}

void C::metodaC() {
    metodaA();
    apub = 0;
    aprot = 0;
    apriv = 0;

    metodaB();
    bpub = 0;
    bprot = 0;
    bpriv = 0;

    metodaC();
    cpub = 0;
    cprot = 0;
    cpriv = 0;
}
