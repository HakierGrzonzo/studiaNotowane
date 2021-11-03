
//
// ZADANIE 7 
//
class Main {
    public static void main(String[] args) {
        int found = 0;
        for (int i = 0; i < 99; i++) {
            double random = Math.random() * 100;
            if (random < 20) {
                found++;
                System.out.println(random);
            }
            if (found == 10) {
                break;
            }
        }
    }
}
