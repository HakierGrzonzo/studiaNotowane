// Zadanie 4
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        System.out.print("Podaj promień koła: ");
        float r = stdin.nextFloat();
        System.out.println("pole to " + (3.14 * r*r));
    }
}
