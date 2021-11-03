//
// ZADANIE 5
//
import java.util.Scanner;
class Main {
    private static float wyznacznik(float a1, float a2, float a3, float a4) {
        float mat[] = {a1, a2, a3, a4};
        return mat[0] * mat[3] - mat[1] * mat[2];
    }
    public static float[] solve(float[] mat) {
        float w = wyznacznik(
            mat[0], mat[1],
            mat[3], mat[4]
        );
        float wx = wyznacznik(
            mat[2], mat[1],
            mat[5], mat[4]
        );
        float wy = wyznacznik(
            mat[0], mat[2],
            mat[3], mat[5]
        );
        return new float[]{wx / w, wy / w};
    }
    public static void main(String[] args) {
        float[] input_mat = {0, 0, 0, 0, 0, 0};
        // input_mat to układ równań w formie:
        // a1   b1  c1
        // a2   b2  c2
        // w indeksach:
        // 0    1   2
        // 3    4   5
        try {
            Scanner stdin = new Scanner(System.in);
            System.out.println("Podaj macierz: ");
            for (int i = 0; i < 6; i++) {
                input_mat[i] = stdin.nextFloat();
            }
        } catch (Exception e) {
            System.out.println("Złe dane wejściowe");
        }
        float w = wyznacznik(
            input_mat[0], input_mat[1],
            input_mat[3], input_mat[4]
        );
        if (w != 0) {
            float[] res = solve(input_mat);
            System.out.println("x = " + res[0]);
            System.out.println("y = " + res[1]);
        } else {
            System.out.println("W = 0");
        }
    }
}
