// Zadanie 2
public class zad2 {
    public static int silnia(int n) {
        if (n > 1) {
            return silnia(n - 1) * n;
        }
        return 1;
    }
    public static void main(String[] args) {
        for (int i = 0; i < 10; i++) {
            System.out.print(i + "\t->\t");
            System.out.println(silnia(i));
        }
    }
}
