// zadanie 4
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        var stdin = new Scanner(System.in);
        System.out.print("Podaj wymiar: ");
        var n = stdin.nextInt();
        var tab = new int[n][n];
        Direction dir = Direction.east;
        int x = -1;
        int y = 0;
        int i = 1;
        while (i < n * n + 1) {
            int newX = x;
            int newY = y;
            switch (dir) {
                case east:
                    newX += 1;
                    break;
                case south:
                    newY += 1;
                    break;
                case west:
                    newX -= 1;
                    break;
                case north:
                    newY -= 1;
                    break;
            }
            if (newX >= 0 && newX < n && newY >= 0 && newY < n) {
                if (tab[newY][newX] != 0) {
                    // rotate
                    switch (dir) {
                        case east:
                            dir = Direction.south;
                            break;
                        case south:
                            dir = Direction.west;
                            break;
                        case west:
                            dir = Direction.north;
                            break;
                        case north:
                            dir = Direction.east;
                            break;
                    }
                } else {
                    x = newX;
                    y = newY;
                    tab[y][x] = i;
                    i++;
                }
            } else {
                // rotate
                switch (dir) {
                    case east:
                        dir = Direction.south;
                        break;
                    case south:
                        dir = Direction.west;
                        break;
                    case west:
                        dir = Direction.north;
                        break;
                    case north:
                        dir = Direction.east;
                        break;
                }
            }
        }
        System.out.println(new Macierz(tab));
    }
}

enum Direction {
    east, south, west, north;
}

class Macierz {
    public int[][] mat;
    public Macierz(int n) {
        mat = new int[n][n];
    }
    public Macierz(int[][] mat) {
        this.mat = mat;
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
