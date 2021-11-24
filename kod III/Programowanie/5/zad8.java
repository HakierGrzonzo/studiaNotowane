//
// ZADANIE 8
//
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.io.*;
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
        try {
            var file = new PrintWriter(new FileWriter("dane.txt", true));
            file.println("foo woo");
            file.println("voo woo");
            file.close();
        } catch (IOException e) {

        }
        /*
        var nums = new ArrayList<Integer>();
        try {
            Scanner stdin = new Scanner(file);
            while (true) {
                nums.add(stdin.nextInt());
            }
        } catch(Exception e) {
        }
        int[] numz = sort(nums.stream().mapToInt(i->i).toArray());
        for (int i = 0; i < numz.length; i++) {
            System.out.println(numz[i]);
        }
        */
    }
}
