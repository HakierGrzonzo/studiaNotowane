
//
// ZADANIE 8 
//
class Main {
    public static void main(String[] args) {
        int rozmiar = 1;
        int liczba = 5;
        for (int i = 0; i < 10; i++) {
            System.out.print(2 * liczba);
            liczba++;
            for (int j = 1; j < rozmiar; j++) {
                System.out.print('\t');
                System.out.print(2 * liczba);
                liczba++;
            }
            System.out.println();
            rozmiar++;
        }
    }
}
