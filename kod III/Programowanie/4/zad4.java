
//
// ZADANIE 4
//
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
class Main {
    public static void main(String[] args) {
        try {
            Pattern regex = Pattern.compile("\\w+");
            BufferedReader stdin = new BufferedReader(new InputStreamReader(System.in));
            int sum = 0;
            while (true) {
                String text = stdin.readLine();
                if (text == null) {
                    // Jeśli tekst się skończył znakiem końca lini
                    // np. <C-d> to zakońć program
                    break;
                }
                Matcher matcher = regex.matcher(text);
                while(matcher.find()) {
                    sum++;
                }
            }
            System.out.println(sum);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
