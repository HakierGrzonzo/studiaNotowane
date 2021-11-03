
//
// ZADANIE 6 - bez regexa
//
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
class Main {
    public static void main(String[] args) {
        try {
            BufferedReader stdin = new BufferedReader(new InputStreamReader(System.in));
            while (true) {
                String arg = args[0];
                String text = stdin.readLine();
                if (text == null) {
                    // Jeśli tekst się skończył znakiem końca lini
                    // np. <C-d> to zakońć program
                    break;
                }
                int i = 0;
                int word_index = 0;
                boolean found = false;
                while (i < text.length()) {
                    char got = text.charAt(i);
                    if (got == ' ' || i == 0) {
                        if (got == ' ') {
                            i++;
                        }
                        word_index = 0;
                        while (text.charAt(i) == arg.charAt(word_index)) {
                            word_index++;
                            i++;
                            if (word_index == arg.length() &&
                                    i == text.length()) {
                                found = true;
                                break;
                            }
                            if (word_index == arg.length() &&
                                    text.charAt(i) == ' ') {
                                found = true;
                                break;
                            }
                            if (word_index == arg.length()) {
                                break;
                            }
                        }
                        i++;
                        if (found) {
                            System.out.println(text);
                            break;
                        }
                    } else {
                        i++;
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
