
//
// ZADANIE 3
//
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
class Main {
    public static void main(String[] args) {
        try {
            Pattern imię = Pattern.compile("Grze((gorz)|(siek))");
            BufferedReader stdin = new BufferedReader(new InputStreamReader(System.in));
            while (true) {
                String text = stdin.readLine();
                if (text == null) {
                    // Jeśli tekst się skończył znakiem końca lini
                    // np. <C-d> to zakońć program
                    break;
                }
                Matcher matcher = imię.matcher(text);
                if (matcher.find()) {
                    System.out.println(text);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
