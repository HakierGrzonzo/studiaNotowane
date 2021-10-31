//
// ZADANIE 6
//

import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        // next pobiera słowa separowane \n lub ' '
        String text = stdin.next();
        do {
            System.out.println(text);
            text = stdin.next();
        } while (!text.equals("quit"));
    }
}
