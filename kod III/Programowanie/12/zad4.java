// Zadanie 4
import java.util.ArrayList;
import java.util.List;

public class zad4 {
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
    public static List<Integer> mergesort(List<Integer> src) {
        if (src.size() < 2) {
            return src;
        } else if (src.size() == 2) {
            var res = new ArrayList<Integer>();
            if (src.get(0) < src.get(1)) {
                res.add(src.get(0));
                res.add(src.get(1));
            } else {
                res.add(src.get(1));
                res.add(src.get(0));
            }
            return res;
        } else {
            int div = src.size() / 2;
            var r1 = new ArrayList<Integer>();
            for (int i = 0; i < div; i++) {
                r1.add(src.get(i));
            }
            var r2 = new ArrayList<Integer>();
            for (int i = div; i < src.size(); i++) {
                r2.add(src.get(i));
            }
            return merge(mergesort(r1), mergesort(r2));
        }
    }
    public static void main(String[] args) {
        var a = new ArrayList<Integer>();
        a.add(5);
        a.add(18);
        a.add(3);
        a.add(17);
        a.add(19);
        a.add(2);
        a.add(11);
        a.add(8);
        a.add(10);
        a.add(12);
        a.add(1);
        a.add(15);
        a.add(9);
        a.add(4);
        a.add(13);
        a.add(20);
        a.add(16);
        a.add(7);
        a.add(6);
        a.add(14);
        System.out.println(mergesort(a));
    }
}
