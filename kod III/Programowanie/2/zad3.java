//
// ZADANIE 3
//
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        try {
            Scanner stdin = new Scanner(System.in);
            System.out.print("Podaj r: ");
            float r = stdin.nextFloat();
            System.out.print("Podaj h: ");
            float h = stdin.nextFloat();
            if (r > 0 && h > 0) {
                System.out.println("Pole powierzchni bocznej: " + (2 * 3.14 * r * h));
                System.out.println("Objętość: " + (3.14 * r * r * h));
            } else {
                System.out.println("Złe dane wejściowe");
            }
        } catch (Exception e) {
            System.out.println("Złe dane wejściowe");
        }
    }
}
