
//
// ZADANIE 6
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
        stdin.close();
        Arrays.sort(nums);
        for (int i = 0; i < n; i++) {
            System.out.println(nums[i]);
        }
    }
}
