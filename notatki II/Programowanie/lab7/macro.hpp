#pragma once
#include <iostream>

#define print(arg) std::cout << __FILE__ << ":" << __LINE__ << " " << arg << std::endl;
#define printName(arg) std::cout << __FILE__ << ":" << __LINE__ << " " << #arg << " = "<< arg << std::endl;

#define DOM print("Konstruktor Domyślny")
#define PAR print("Konstruktor Parametryczny")
#define DES print("Destruktor")

#define PI 3.14

#define sqr(x) (x * x)
