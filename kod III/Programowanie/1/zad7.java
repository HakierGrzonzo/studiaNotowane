// Zadanie 7
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
        float[] B = {1, 2, 5, 3};
        float[] A = {1, 2, 5};
        System.out.println("B(x) = " + horner(B, x));
        System.out.println("A(x) = " + horner(A, x));
    }
}
