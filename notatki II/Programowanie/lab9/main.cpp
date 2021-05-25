#include "macro.hpp"
#include "class.hpp"

int main() {
    zespolona test;
    printName(test++);
    printName(test++);
    printName(++test);
    zespolona druga = zespolona(5, 6);
    printName(druga);
    printName(test + druga);
    printName(test - druga);
    printName((test == druga));
    printName((druga == druga));
}
