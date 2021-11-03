//
// ZADANIE 2
//
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
class Main {
    public static void main(String[] args) {
        try {
            Pattern regex = Pattern.compile("(?<foo>[0-9]+(\\.[0-9]+)?)");
            BufferedReader stdin = new BufferedReader(new InputStreamReader(System.in));
            String text = stdin.readLine();
            Matcher matcher = regex.matcher(text);
            double sum = 0;
            while (matcher.find()) {
                sum += Double.parseDouble(matcher.group("foo"));
            }
            System.out.println(sum);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
