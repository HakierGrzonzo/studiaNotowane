//Zadanie 4
import javax.swing.*;
import java.awt.*;

class Main {
    public static void main(String[] args) {
        JFrame frame = new JFrame("test");
        frame.setDefaultCloseOperation(frame.EXIT_ON_CLOSE);
        JLabel label = new JLabel("Witaj świecie!");
        label.setFont(new Font("serif", Font.PLAIN, 36));
        frame.getContentPane().add(label);
        frame.setVisible(true);
    }
}
