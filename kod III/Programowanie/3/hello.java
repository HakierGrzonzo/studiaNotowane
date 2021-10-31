//
// ZADANIE 1
//

import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        String text = "";
        do {
            System.out.print(text);
            text = stdin.nextLine();
            text += "\n";
        } while (!text.equals("quit\n"));
    }
}
