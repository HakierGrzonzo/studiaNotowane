// Zadanie 1
import java.io.*;
import java.util.*;
class Main {
    public static void main(String[] args) {
        var scanner = new Scanner(System.in);
        double pi = 3.14;
        try {
            System.out.print("Podaj r: ");
            var r = scanner.nextDouble();
            if (r <= 0) {
                throw new Exception();
            }
            System.out.print("Podaj l: ");
            var l = scanner.nextDouble();
            if (l <= 0 && l > r) {
                throw new Exception();
            }
            System.out.println("Pole powierzchni: " + (pi * r * (r + l)));
            double h = Math.sqrt(l * l - r * r);
            System.out.println("Objętość: " + ((1.0/3.0) * pi * r * r * h));
        } catch (Exception e) {
            System.out.println("Zły format argumentu!");
        }
    }
}
