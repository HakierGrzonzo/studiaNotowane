// Zadanie 1
public class zad1 {
    public static int silnia(int n) {
        int res = 1;
        for (int i = 2; i <= n; i++) {
            res *= i;
        }
        return res;
    }
    public static void main(String[] args) {
        for (int i = 0; i < 10; i++) {
            System.out.print(i + "\t->\t");
            System.out.println(silnia(i));
        }
    }
}
