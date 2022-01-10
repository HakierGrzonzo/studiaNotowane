
// Zadanie 5
import java.util.ArrayList;
import java.util.List;

public class zad5 {
    public static List<Integer> merge(List<Integer> a, List<Integer> b) {
        var res = new ArrayList<Integer>();
        for (int i = 0; i < a.size(); i++) {
            res.add(a.get(i));
        }
        for (int i = 0; i < b.size(); i++) {
            res.add(b.get(i));
        }
        return res;
    }
    public static List<Integer> fastsort(List<Integer> src) {
        if (src.size() < 2) {
            return src;
        } else {
            int div = src.get(src.size() - 1);
            var rl = new ArrayList<Integer>();
            var re = new ArrayList<Integer>();
            var rg = new ArrayList<Integer>();
            for (int i = 0; i < src.size(); i++) {
                var n = src.get(i);
                if (n > div) {
                    rg.add(n);
                } else if (n == div) {
                    re.add(n);
                } else {
                    rl.add(n);
                }
            }
            return merge(merge(fastsort(rl), fastsort(re)), fastsort(rg));
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
        System.out.println(fastsort(a));
    }
}
