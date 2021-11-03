// Zadanie 6
import java.util.Scanner;
class Main {
    public static float horner(float[] array, float x) {
        float wynik = array[0];
        for (int i = 1; i < array.length; i++) {
            wynik = wynik * x + array[i];
        }
        return wynik;
    }
    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        System.out.print("Podaj x: ");
        float x = stdin.nextFloat();
        final float a = 1;
        final float b = 2;
        final float c = 5;
        final float d = 3;
        float A = x * x * a + x * b + c;
        float B = x * x * x * a + x * x * b + x * c + d;
        System.out.println("B(x) = ax³ + bx² + cx + d = " + B);
        System.out.println("A(x) = ax² + bx + c = " + A);
    }
}
