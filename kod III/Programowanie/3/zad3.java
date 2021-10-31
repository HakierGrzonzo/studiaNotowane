//
// ZADANIE 3
//

import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        String text = stdin.nextLine();
        do {
            Boolean is_in_whitespace = false;
            for(char x : text.toCharArray()) {
                // taby też są jakimś znakiem odstępami
                if (x == ' ' || x == '\t') {
                    if (!is_in_whitespace) {
                        System.out.print(x);
                        is_in_whitespace = true;
                    }
                } else {
                    System.out.print(x);
                    is_in_whitespace = false;
                }
            }
            System.out.print("\n");
            text = stdin.nextLine();
        } while (!text.equals("quit"));
    }
}
