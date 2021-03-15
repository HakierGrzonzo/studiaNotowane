#pragma once

#include <string>
#include <iostream>

using namespace std;

class Test {
    private:
        int selfID;
        string name;
    public:
        static int id;
        Test();
        Test(string _name);
        ~Test();
};
