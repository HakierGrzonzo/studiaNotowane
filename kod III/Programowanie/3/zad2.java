//
// ZADANIE 2
//

import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        String text = stdin.nextLine();
        do {
            int tmp = 0;
            for(char x : text.toCharArray()) {
                if (x == 'a') {
                    tmp++;
                }
            }
            System.out.println(tmp);
            text = stdin.nextLine();
        } while (!text.equals("quit"));
        stdin.close();
    }
}
