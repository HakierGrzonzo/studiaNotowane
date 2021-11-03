//
// ZADANIE 2
//

import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        System.out.print("Podaj a: ");
        float a = stdin.nextFloat();
        System.out.print("Podaj b: ");
        float b = stdin.nextFloat();
        if (a == 0) {
            System.out.println("a == 0");
        } else {
            System.out.println(-(b/a));
        }
    }
}
