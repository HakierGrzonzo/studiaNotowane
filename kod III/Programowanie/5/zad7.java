//
// ZADANIE 7
//
import java.util.Scanner;
import java.util.Arrays;
class Main {
    public static int[] sort(int[] nums) {
        int[] res = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            res[i] = nums[i];
        }
        Arrays.sort(res);
        for (int i = 0; i < nums.length / 2; i++) {
            int tmp = res[i];
            res[i] = res[nums.length - i - 1];
            res[nums.length - 1 - i] = tmp;
        }
        return res;
    }
    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        System.out.print("Podaj n: ");
        int n = stdin.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = stdin.nextInt();
        }
        stdin.close();
        nums = sort(nums);
        for (int i = 0; i < n; i++) {
            System.out.println(nums[i]);
        }
    }
}
