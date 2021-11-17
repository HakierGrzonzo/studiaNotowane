
//
// ZADANIE 4
//
import java.text.Collator;
import java.util.*;
class Main {
    public static void main(String[] args) {
        var pracownicy = new ArrayList<Pracownik>();
        pracownicy.add(new Pracownik(0, "Adam", "Hanik", "dev"));
        pracownicy.add(new Pracownik(0, "John", "Addams", "dev"));
        pracownicy.add(new Pracownik(0, "Bill", "Bonks", "ceo"));
        pracownicy.add(new Pracownik(0, "Will", "Smith", "azure"));
        Collections.sort(pracownicy);
        System.out.println(pracownicy);
    }
}

class Pracownik implements Comparable {
    private int id;
    private String name;
    private String surname;
    private String position;
    private Collator collator;
    public Pracownik(int id, String name, String surname, String position) {
        this.id = id;
        this.name = name;
        this.surname = surname;
        this.position = position;
        collator = Collator.getInstance(new Locale("pl", "PL"));
    }

    public String toString() {
        return "<Pracownik " + id + ": "+ position + "; " + surname + " " + name + ">";
    }

    public String getName() {
        return surname;
    }
    
    @Override()
    public int compareTo(Object other) {
        if (this.getClass() == other.getClass()) {
            Pracownik other_obj = (Pracownik) other;
            int res = collator.compare(this.position, other_obj.position);
            if (res == 0) {
                res = collator.compare(this.surname, other_obj.surname);
            }
            return res;
        } else {
            return 0;
        }
    }
}

