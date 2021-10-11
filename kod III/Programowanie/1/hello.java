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
        /* 1
        System.out.print("Grzegorz Koperwas ");
        System.out.println(2021 - 2001);
        */
        /* 2
        System.out.print("X X\n X\nX X");
        */
        Scanner stdin = new Scanner(System.in);
        /* 3
        System.out.print("Podaj a: ");
        float a = stdin.nextFloat();
        System.out.print("Podaj b: ");
        float b = stdin.nextFloat();
        System.out.println("a + b = " + (a + b));
        System.out.println("a - b = " + (a - b));
        System.out.println("a * b = " + (a * b));
        System.out.println("a / b = " + (a / b));
        */
        /* 4
        System.out.print("Podaj promień koła: ");
        float r = stdin.nextFloat();
        System.out.println("pole to " + (3.14 * r*r));
        */
        /* 6
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
        */
        /* 7
        float[] B = {1, 2, 5, 3};
        float[] A = {1, 2, 5};
        System.out.println("B(x) = " + horner(B, x));
        System.out.println("A(x) = " + horner(A, x));
        */
        
        System.out.print("Podaj r: ");
        float r = stdin.nextFloat();
        System.out.print("Podaj h: ");
        float h = stdin.nextFloat();
        System.out.println("Pole powierzchni bocznej: " + (2 * 3.14 * r * h));
        System.out.println("Objętość: " + (3.14 * r * r * h));
    }
}
