import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        String stl = "01:23U";
        System.out.println(stl.split(":")[1]);
        String sgl = "01|23U";
        System.out.println(sgl.split("\\|")[1]);
    }
}
