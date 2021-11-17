//
// ZADANIE 2
//
import java.text.Collator;
import java.util.*;
class Main {
    public static void main(String[] args) {
        Telefon telefon = new Telefon();
        telefon.addContact(new Dane("112", "Numer alarmowy"));
        telefon.addContact(new Dane("997", "Policja"));
        telefon.addContact(new Dane("#*4", "Stan Konta"));
        telefon.addContact(new Dane("384 286 107", "Alicja"));
        telefon.sort();
        System.out.println(telefon);
    }
}

class Dane implements Comparable {
    private String numer;
    private String name;
    private Collator collator;
    public Dane(String numer_, String name_) {
        numer = numer_;
        name = name_;
        collator = Collator.getInstance(new Locale("pl", "PL"));
    }

    public String toString() {
        return "<Dane: "+ name + "; " + numer + ">";
    }

    public String getName() {
        return name;
    }
    
    @Override()
    public int compareTo(Object other) {
        Dane other_obj = (Dane) other;
        return collator.compare(name, other_obj.getName());
    }
}

class Telefon {
    ArrayList<Dane> kontakty = new ArrayList<Dane>();
    public void addContact(Dane kontakt) {
        kontakty.add(kontakt);
    }
    public String toString() {
        String res = "<Telefon: [";
        for (Dane kontakt : kontakty) {
            res += kontakt.toString() + ", ";
        }
        return res + "]>";
    }
    public void sort() {
        Collections.sort(kontakty);
    }
}
