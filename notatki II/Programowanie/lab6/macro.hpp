#pragma once
#include <iostream>

#define print(arg) std::cout << __FILE__ << ":" << __LINE__ << " " << arg << std::endl;
#define printName(arg) std::cout << __FILE__ << ":" << __LINE__ << " " << #arg << " = "<< arg << std::endl;
