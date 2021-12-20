//Zadanie 1
import javax.swing.*;

class Main {
    public static void main(String[] args) {
        JFrame frame = new JFrame("test");
        frame.setDefaultCloseOperation(frame.EXIT_ON_CLOSE);
        frame.getContentPane().add(new JLabel("Hello World"));
        frame.setVisible(true);
    }
}
