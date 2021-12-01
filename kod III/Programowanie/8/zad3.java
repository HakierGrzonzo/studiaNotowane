// Zadanie 3
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        var stdin = new Scanner(System.in);
        System.out.print("Podaj wymiar: ");
        int i = stdin.nextInt();
        var m1 = new Macierz(i);
        for (int y = 0; y < i; y++) {
            for (int x = 0; x < i; x++) {
                System.out.print("Podaj m[" + y + "][" + x + "]: ");
                m1.mat[y][x] = stdin.nextDouble();
            }
        }
        var w1 = new Wektor(i);
        for (int x = 0; x < i; x++) {
            System.out.print("Podaj w[" + x + "]: ");
            w1.mat[x] = stdin.nextDouble();
        }
        var algos = new Algorytm();
        var res = algos.macierzXwektor(m1, w1);
        var m1str = m1.toString().split("\n");
        var w1str = w1.toString().split("\n");
        var resstr = res.toString().split("\n");
        boolean printedSign = false;
        for (int j = 0; j < i; j++) {
            if ((j + 1) * 2 > i && !printedSign) {
                System.out.println(m1str[j] + " • " + w1str[j] + " = " + resstr[j]);
                printedSign = true;
            } else {
                System.out.println(m1str[j] + "   " + w1str[j] + "   " + resstr[j]);
            }
        }
    }
}

class Wektor {
    public double[] mat;
    public Wektor(int n) {
        this.mat = new double[n];
    }
    public Wektor(double[] mat) {
        this.mat = mat;
    }
    public double x() {
        return this.mat[0];
    }
    public double y() {
        return this.mat[1];
    }
    public double iloczynSkalarny(Wektor other) {
        return this.x() * other.x() + this.y() * other.y();
    }
    public String toString() {
        String res = "";
        for (int i = 0; i < this.mat.length; i++) {
            res += "\n|\t" + mat[i] + "\t|";
        }
        return res.substring(1);
    }
}

class Macierz {
    public double[][] mat;
    public Macierz(int n) {
        mat = new double[n][n];
    }
    public Wektor multiply(Wektor w2) {
        double[] resMat = new double[mat.length];
        var vecMat = w2.mat;
        for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat[i].length; j++) {
                resMat[i] += mat[i][j] * vecMat[i];
            }
        }
        return new Wektor(resMat);
    }
    public String toString() {
        String res = "";
        for (int i = 0; i < mat.length; i++) {
            res += "\n|\t";
            for (int j = 0; j < mat[i].length; j++) {
                res += mat[i][j] + "\t";
            }
            res += "|";
        }
        return res.substring(1);
    }
}

class Algorytm {
    public double iloczynSkalarnyW2(Wektor w1, Wektor w2) {
        return w1.iloczynSkalarny(w2);
    }
    public Wektor macierzXwektor(Macierz m, Wektor w) {
        return m.multiply(w);
    }
}
