#include "class.hpp"

int Test::id = 0;

Test::Test() {
    name = "noname";
    selfID = id;
    id++;
    cout << "hello from " << name << " Z id " << selfID <<  endl;
}

Test::~Test() {
    cout << "Papa " << name << "; Z id: " << selfID << endl;
}

Test::Test(string _name) {
    name = _name;
    selfID = id;
    id++;
    cout << "hello from " << name << " Z id " << selfID <<  endl;
}
