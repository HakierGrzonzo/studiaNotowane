//
// ZADANIE 1
//

import java.util.ArrayList;
class Main {
    public static void main(String[] args) {
        Telefon telefon = new Telefon();
        telefon.addContact(new Dane("112", "Numer alarmowy"));
        telefon.addContact(new Dane("997", "Policja"));
        telefon.addContact(new Dane("#*4", "Stan Konta"));
        System.out.println(telefon);
    }
}

class Dane {
    String numer;
    String name;
    public Dane(String numer_, String name_) {
        numer = numer_;
        name = name_;
    }
    public String toString() {
        return "<Dane: "+ name + "; " + numer + ">";
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
}
