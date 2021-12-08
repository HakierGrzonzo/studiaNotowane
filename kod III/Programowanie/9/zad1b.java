//Zadanie 1 - utf8

import java.util.Scanner;
import java.io.PrintWriter;
import java.io.FileWriter;
import java.io.File;
import java.nio.charset.*;
import java.io.FileNotFoundException;

class Main {
    public static void main(String[] args) {
        File file = new File("dane.txt");
        File outFile = new File("wynik.txt");
        try {
            Scanner scanner = new Scanner(file, "utf8");
            double x1 = scanner.nextDouble();
            double y1 = scanner.nextDouble();
            double x2 = scanner.nextDouble();
            double y2 = scanner.nextDouble();
            PrintWriter out = new PrintWriter(new FileWriter(outFile, StandardCharsets.UTF_8));
            out.println(Math.hypot(x1 - x2, y1 - y2));
            out.close();
            scanner.close();
        } catch (FileNotFoundException e) {
            System.err.println("Plik nie istnieje!");
        } catch (Exception e) {
            System.err.println("Plik ma niepoprawny format");
        }
    }
}
