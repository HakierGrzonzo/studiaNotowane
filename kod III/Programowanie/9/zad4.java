//Zadanie 4

import java.util.Scanner;
import java.io.PrintWriter;
import java.io.FileWriter;
import java.io.File;
import java.nio.charset.*;
import java.io.FileNotFoundException;

class Main {
    public static void main(String[] args) {
        System.out.print("Podaj ścieżkę: ");
        Scanner stdin = new Scanner(System.in);
        File file = new File(stdin.nextLine());
        stdin.close();
        try {
            var in = new Scanner(file, "cp1252");
            while (true) System.out.println(in.nextLine());
        } catch (FileNotFoundException e) {
            System.err.println("Plik nie istnieje!");
        } catch (Exception e) {
        }
    }
}
