//
// ZADANIE 4
//

import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        String text = stdin.nextLine();
        Integer tmp = 0;
        do {
            Boolean was_a = false;
            for(char x : text.toCharArray()) {
                // taby też są jakimś znakiem odstępami
                if (x == 'a') {
                    was_a = true;
                } else if (x == 'b' && was_a) {
                    was_a = false;
                    tmp++;
                } else {
                    was_a = false;
                }
            }
            text = stdin.nextLine();
        } while (!text.equals("quit"));
        System.out.println(tmp);
    }
}
