//Zadanie 1

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        var algos = new Algorytm();
        algos.setAB(1, 1);
    }
}

class Algorytm {
    private double a = 0;
    private double b = 0;
    public void setAB(double a, double b) {
        this.a = a;
        this.b = b;
    }
}
