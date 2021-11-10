//
// ZADANIE 3
//
import java.util.Scanner;
import java.util.Arrays;
class Main {
    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        System.out.print("Podaj n: ");
        int n = stdin.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = stdin.nextInt();
        }
        Arrays.sort(nums);
        System.out.println("Maksymalna liczba: " + nums[n-1]);
        System.out.println("Minimalna liczba: " + nums[0]);
        stdin.close();
    }
}
