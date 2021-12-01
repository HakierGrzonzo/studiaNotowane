// Zadanie 2
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        var w1 = new Wektor2(1, 1);
        var w2 = new Wektor2(-1, 0.5);
        var algos = new Algorytm();
        System.out.println(algos.iloczynSkalarnyW2(w1, w2));
    }
}

class Wektor2 {
    public double x = 0;
    public double y = 0;
    public Wektor2(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public double iloczynSkalarny(Wektor2 other) {
        return this.x * other.x + this.y * other.y;
    }
}

class Algorytm {
    public double iloczynSkalarnyW2(Wektor2 w1, Wektor2 w2) {
        return w1.iloczynSkalarny(w2);
    }
}
