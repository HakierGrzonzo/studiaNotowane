// zadanie 8
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        System.out.print("Podaj r: ");
        float r = stdin.nextFloat();
        System.out.print("Podaj h: ");
        float h = stdin.nextFloat();
        System.out.println("Pole powierzchni bocznej: " + (2 * 3.14 * r * h));
        System.out.println("Objętość: " + (3.14 * r * r * h));
    }
}
