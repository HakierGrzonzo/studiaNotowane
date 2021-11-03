

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
            Pattern regex = Pattern.compile("[0-3]?[0-9]-[0-1]?[0-9]-[0-9]+");
            BufferedReader stdin = new BufferedReader(new InputStreamReader(System.in));
            String text = stdin.readLine();
            Matcher matcher = regex.matcher(text);
            if (matcher.find()) {
                System.out.println("Dobrze!");
            } else {
                System.out.println("Źle!");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
