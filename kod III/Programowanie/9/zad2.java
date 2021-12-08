//Zadanie 2

import java.util.Scanner;
import java.io.PrintWriter;
import java.io.FileWriter;
import java.io.File;
import java.nio.charset.*;
import java.io.FileNotFoundException;

class Main {
    public static void main(String[] args) {
        File outFile = new File("losowe.txt");
        try {
            Scanner scanner = new Scanner(System.in);
            System.out.print("Podaj n: ");
            int n = scanner.nextInt();
            PrintWriter out = new PrintWriter(new FileWriter(outFile, StandardCharsets.ISO_8859_1));
            for (int i = 0; i < n; i++) out.println(Math.random() * n);
            out.close();
            scanner.close();
        } catch (FileNotFoundException e) {
            System.err.println("Plik nie istnieje!");
        } catch (Exception e) {
            System.err.println("Plik ma niepoprawny format");
        }
    }
}
