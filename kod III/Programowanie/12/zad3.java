import java.util.ArrayList;
import java.util.List;

// Zadanie 3
public class zad3 {
    public static List<Integer> merge(List<Integer> a, List<Integer> b) {
        var res = new ArrayList<Integer>();
        int pointer_a = 0;
        int pointer_b = 0;
        while ((pointer_a < a.size()) && (pointer_b < b.size())) {
            if (a.get(pointer_a) < b.get(pointer_b)) {
                res.add(a.get(pointer_a));
                pointer_a++;
            } else {
                res.add(b.get(pointer_b));
                pointer_b++;
            }
        }
        while (pointer_a < a.size()) {
            res.add(a.get(pointer_a));
            pointer_a++;
        }
        while (pointer_b < b.size()) {
            res.add(b.get(pointer_b));
            pointer_b++;
        }
        return res;
    }
    public static void main(String[] args) {
        var a = new ArrayList<Integer>();
        var b = new ArrayList<Integer>();
        a.add(0);
        a.add(1);
        a.add(3);
        a.add(4);
        b.add(2);
        b.add(5);
        System.out.println(merge(a, b));
    }
}
