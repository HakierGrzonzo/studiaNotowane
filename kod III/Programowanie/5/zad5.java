//
// Zadanie 5
//
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        int[] some_nums = {1, 2, 4, -5};
        Algorytm algorytm = new Algorytm(some_nums);
        System.out.println("min: " + some_nums[algorytm.indeks_min()]);
        System.out.println("Średnia: " + algorytm.mean());
    }
}
class Algorytm {
    int[] nums;
    public Algorytm(int[] nums_) {
        nums = nums_;
    }
    public int indeks_min() {
        int res = nums[0];
        int indeks = 0;
        for (int i = 0; i < nums.length; i++) {
            if (res > nums[i]) {
                indeks = i;
                res = nums[i];
            }
        }
        return indeks;
    }
    public float mean() {
        float sum = 0; // Wynik ma być nie zaokrąglony
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
        }
        return sum / nums.length;
    }
}
