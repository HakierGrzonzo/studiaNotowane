// zadanie 4
import java.io.*;
import java.util.*;
class Main {
    public static void main(String[] args) {
        var workers = new ArrayList<Worker>();
        workers.add(new Worker(1, "Koperwas", 56.40));
        workers.add(new Worker(2, "Kowalczyk", 20));
        workers.add(new Worker(3, "Koper", 18.30));
        Collections.sort(workers);
        System.out.println(workers);
    }
}

class Worker implements Comparable {
    private int id;
    private String surname;
    private double pay; // powinno być intem w groszówkach
    public Worker(int id, String surname, double pay) {
        this.id = id;
        this.surname = surname;
        this.pay = pay;
    }
    public int compareTo(Object other) {
        if (other.getClass() == this.getClass()) {
            Worker o = (Worker) other;
            if (this.pay == o.pay) {
                return 0;
            } else {
                boolean greater = this.pay > o.pay;
                int res = -1;
                if (greater) res = -res;
                return res;
            }
        } else {
            return 0;
        }
    }
    public String toString() {
        return "<Worker " + this.id + " " + this.surname + " " + this.pay + ">";
    }
}

