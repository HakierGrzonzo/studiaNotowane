#include <string>
#include <iostream>
#include <fstream>

#include "class.hpp"

using namespace std;

Test globalnyTest;

void zjadamRam() {
    // destruktor mnie nie zje a ja zjem ram
    Test* testptr = new Test("rameater");
    Test test = Test("not_rameater");
}

int main()
{
    Test test = Test("mainowy");
    Test* testowa = new Test("testowa");
    delete testowa;
    zjadamRam();
    cout << "Do widzenia!" << endl;
}

Test globalnyTest2 = Test("hehehe");
