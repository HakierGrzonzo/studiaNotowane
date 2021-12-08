//Zadanie 3 - utf8

import java.util.Scanner;
import java.io.PrintWriter;
import java.io.FileWriter;
import java.io.File;
import java.nio.charset.*;
import java.io.FileNotFoundException;

class Main {
    public static void main(String[] args) {
        System.out.print("Podaj ścierzkę: ");
        Scanner stdin = new Scanner(System.in);
        File file = new File(stdin.nextLine());
        stdin.close();
        try {
            PrintWriter out = new PrintWriter(new FileWriter(file, StandardCharsets.UTF_8));
            out.print("Polskie znaki: ąęćłóśżź");
            out.close();
        } catch (FileNotFoundException e) {
            System.err.println("Plik nie istnieje!");
        } catch (Exception e) {
            System.err.println("Plik ma niepoprawny format");
        }
    }
}
