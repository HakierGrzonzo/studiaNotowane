//
// ZADANIE 5/6
//
import java.text.Collator;
import java.util.*;
class Main {
    public static void main(String[] args) {
        var books = new ArrayList<Book>();
        books.add(new Book(0, "book_a", "xyz"));
        books.add(new Book(1, "book_b", "xyz"));
        books.add(new Book(2, "book_a", "abc"));
        books.add(new Book(3, "book_b", "abc"));
        Collections.sort(books);
        System.out.println(books);
    }
}

class Book implements Comparable {
    private int id;
    private String title;
    private String author;
    private Collator collator;
    public Book(int id, String title, String author) {
        this.id = id;
        this.title = title;
        this.author = author;
        collator = Collator.getInstance(new Locale("pl", "PL"));
    }

    public String toString() {
        return "<Książka " + id + ": "+ title + "; " + author + ">";
    }

    @Override()
    public int compareTo(Object other) {
        if (this.getClass() == other.getClass()) {
            Book other_obj = (Book) other;
            int res = collator.compare(this.author, other_obj.author);
            if (res == 0) {
                res = collator.compare(this.title, other_obj.title);
            }
            return res;
        } else {
            return 0;
        }
    }
}

