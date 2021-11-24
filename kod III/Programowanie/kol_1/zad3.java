// zadanie 3
import java.io.*;
import java.util.*;
class Main {
    public static void main(String[] args) {
        if (args.length == 1) {
            try {
                var file = new File(args[0]);
                var scanner = new Scanner(file);
                while (true) {
                    try {
                        System.out.println(scanner.nextLine());
                    } catch (NoSuchElementException e) {
                        break;
                    }
                }
                scanner.close();
            } catch (IOException e) {
                System.out.println("Plik nie istnieje lub nie masz do niego uprawnień!");
            } 
        } else {
            System.out.println("Podaj nazwę pliku jako argument");
        }
    }
}

