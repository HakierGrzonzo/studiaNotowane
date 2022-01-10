// zadanie 2
import java.io.*;
import java.util.*;
class Main {
    public static void main(String[] args) {
        try {
            var file = new File(args[0]);
            try {
                var scanner = new Scanner(file);
                var list = new ArrayList<Double>();
                try {
                    while (true) {
                        list.add(new Double(scanner.nextDouble()));
                    }
                } catch (Exception e) {}
                var sorted = new Algorytm().sort(list);
                System.out.println(list);
                System.out.println(sorted);
                scanner.close();
            } catch (FileNotFoundException e) {
                System.err.println("Plik nie istnieje!");
            }
        } catch (ArrayIndexOutOfBoundsException e) {
            System.err.println("Nie podano pliku!");
        }
    }
}

class Algorytm {
    public List<Double> sort(List<Double> nums) {
        // Nie sortujemy in-place, tylko nasza metoda jest `pure function`
        List<Double> tmp = new ArrayList<Double>(nums);
        boolean has_swaped = true;
        while (has_swaped) {
            has_swaped = false;
            for (int i = 0; i < tmp.size() - 1; i++) {
                if (tmp.get(i) > tmp.get(i + 1)) {
                    has_swaped = true;
                    var t = tmp.get(i);
                    tmp.set(i, tmp.get(i + 1));
                    tmp.set(i + 1, t);
                }
            }
        }
        return tmp;
    }
}
