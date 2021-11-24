// zadanie 2
import java.io.*;
import java.util.*;
class Main {
    public static void main(String[] args) {
        var scanner = new Scanner(System.in);
        System.out.print("Podaj ilość liczb: ");
        int n = scanner.nextInt();
        double[] liczby = new double[n];
        for (int i = 0; i < n; i++) {
            liczby[i] = scanner.nextDouble();
        }
        var index = Algorytm.max_index(liczby);
        System.out.println("Indeks największego to: " + index);
        System.out.println("liczby[" + index + "] = " + liczby[index]);
        scanner.close();
    }
}

class Algorytm {
    public static int max_index(double[] nums) {
        int found = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[found]) {
                found = i;
            }
        }
        return found;
    }
}
