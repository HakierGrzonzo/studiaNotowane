//
// ZADANIE 1
//

import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        float a = stdin.nextFloat();
        float b = stdin.nextFloat();
        System.out.println("a + b = " + (a+b));
        if (b == 0) {
            System.out.println("Dzielenie przez zero!");
        } else {
            System.out.println("a / b = " + (a/b));
        }
    }
}
