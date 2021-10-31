//
// ZADANIE 5
//

import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        // next pobiera słowa separowane \n lub ' '
        String text = stdin.next();
        Integer i = 0;
        do {
            i++;
            text = stdin.next();
        } while (!text.equals("quit"));
        System.out.println(i);
    }
}
