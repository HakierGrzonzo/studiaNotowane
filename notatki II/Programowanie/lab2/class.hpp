#pragma once

class Cosiek {
    public:
        void info();
        Cosiek(int _numerek = 69);
        Cosiek(const Cosiek &org);
        ~Cosiek();
        int* numerek;
};
