// zadanie 4
import java.io.*;
import java.util.*;
class Main {
    public static void main(String[] args) {
        var p = new PracownikProjekt("foo", "bar", 10);
    }
}

class Pracownik {
    public double wynagrodzenie;
    public Pracownik(double wynagrodzenie) {
        this.wynagrodzenie = wynagrodzenie;
    }
}

class PracownikProjekt extends Pracownik {
    public String nazwaProjektu;
    public String opisProjektu;
    public PracownikProjekt(String nazwaProjektu, String opisProjektu, double wynagrodzenie) {
        /* 
         * W tym przypadku użycie konstuktora bazowego jest wymagane, ponieważ
         * klasa bazowa `Pracownik` nie posiada konstuktora domyślnego.
         *
         * (openjdk 17.0.1 2021-10-19)
         */
        super(wynagrodzenie);
        this.nazwaProjektu = nazwaProjektu;
        this.opisProjektu = opisProjektu;
    }
}
