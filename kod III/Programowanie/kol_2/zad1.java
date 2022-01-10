// zadanie 1
import java.io.*;
import java.util.*;
class Main {
    public static void main(String[] args) {
        var scanner = new Scanner(System.in);
        // w1
        double[] w1 = new double[2];
        System.out.print("Podaj x1: ");
        w1[0] = scanner.nextDouble();
        System.out.print("Podaj y1: ");
        w1[1] = scanner.nextDouble();
        // w2
        double[] w2 = new double[2];
        System.out.print("Podaj x2: ");
        w2[0] = scanner.nextDouble();
        System.out.print("Podaj y2: ");
        w2[1] = scanner.nextDouble();
        var alg = new Algorytm();
        var res = alg.iloczyn_skalarny(w1, w2);
        System.out.println("Iloczyn skalarny to: " + res);
        scanner.close();
    }
}

class Algorytm {
    public double iloczyn_skalarny(double[] w1, double[] w2) {
        return w1[0] * w2[0] + w1[1] * w2[1];
    }
}
