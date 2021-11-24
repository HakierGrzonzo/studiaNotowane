// zadanie 5
import java.io.*;
import java.text.Collator;
import java.util.*;
class Main {
    public static void main(String[] args) {
        var albums = new ArrayList<Music>();
        albums.add(new Music(1, "Stosunki międzynarodowe", "Nocny Kochanek", 56.40, false));
        albums.add(new Music(2, "Stosunki międzynarodowe", "Nocny Kochanek", 56.40, true));
        albums.add(new Music(3, "Stosunki międzynarodowe", "Nocny Kochanek", 56.40, true));
        albums.add(new Music(4, "Hewi Metla", "Nocny Kochanek", 52.40, false));
        albums.add(new Music(5, "Hewi Metla", "Nocny Kochanek", 52.40, true));
        albums.add(new Music(6, "Disco Panzer", "Alan", 52.40, false));
        albums.add(new Music(7, "Polewaj", "Alan", 52.40, false));
        Collections.sort(albums);
        for (Music album : albums) {
            System.out.println(album);
        }
    }
}

class Music implements Comparable {
    private int id;
    private String name;
    private String artist;
    private double cost; // powinno być intem w groszówkach
    private boolean isLeased; 
    private static Collator cmp = Collator.getInstance(new Locale("pl"));
    public Music(int id, String name, String artist, double cost, boolean isLeased) {
        this.id = id;
        this.name = name;
        this.artist = artist;
        this.cost = cost;
        this.isLeased = isLeased;
    }
    public int compareTo(Object other) {
        if (other.getClass() == this.getClass()) {
            Music o = (Music) other;
            int ret = cmp.compare(this.artist, o.artist);
            if (ret == 0) {
                ret = cmp.compare(this.name, o.name);
            }
            if (ret == 0 && this.isLeased != o.isLeased) {
                if (this.isLeased) ret = 1; else ret = -1;
            }
            return ret;
        } else {
            return 0;
        }
    }
    public String toString() {
        return "<Album " + this.name + " by " + this.artist + " isLeased: " + this.isLeased + ">";
    }
}

