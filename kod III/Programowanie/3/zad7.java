//
// ZADANIE 7
//

import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        String text = stdin.nextLine();
        do {
            Boolean got_to_words = false;
            for(char x : text.toCharArray()) {
                if (x == ' ' || x == '\t') {
                    if (got_to_words) {
                        System.out.print(x);
                    }
                } else {
                    System.out.print(x);
                    got_to_words = true;
                }
            }
            System.out.print("\n");
            text = stdin.nextLine();
        } while (!text.equals("quit"));
    }
}
