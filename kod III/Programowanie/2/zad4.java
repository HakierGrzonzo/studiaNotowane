//
// ZADANIE 4
//
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        try {
            Scanner stdin = new Scanner(System.in);
            System.out.print("Podaj a: ");
            float a = stdin.nextFloat();
            System.out.print("Podaj b: ");
            float b = stdin.nextFloat();
            System.out.print("Podaj c: ");
            float c = stdin.nextFloat();
            if (a != 0) {
                double delta = b * b - 4 * a * c;
                if (delta > 0) {
                    delta = Math.sqrt(delta);
                    double x1 = (-b + delta) / (2 * a);
                    double x2 = (-b - delta) / (2 * a);
                    System.out.println("x1: " + x1);
                    System.out.println("x2: " + x2);
                } else if (delta == 0) {
                    System.out.println("x = " + (-b / (2*a)));
                } else {
                    System.out.println("Nie ma rozwiązań");
                }
            }
        } catch (Exception e) {
            System.out.println("Złe dane wejściowe");
        }
    }
}
