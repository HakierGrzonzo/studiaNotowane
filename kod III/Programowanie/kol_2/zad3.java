//Zadanie 3
import javax.swing.*;
import java.awt.*;
class Main {
    public static void main(String[] args) {
        JFrame frame = new JFrame("test");
        frame.setDefaultCloseOperation(frame.EXIT_ON_CLOSE);
        frame.getContentPane().add(new Elipsis());
        frame.pack();
        frame.setVisible(true);
    }
}

class Elipsis extends JPanel {
    public Dimension getPreferrdSize() {
        return new Dimension(200, 200);
    }

    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.RED);
        g.fillRect(40, 60, 90, 50);
        var hsb = Color.RGBtoHSB(0, 128, 128, new float[3]);
        g.setColor(Color.getHSBColor(hsb[0], hsb[1], hsb[2]));
        g.fillOval(40, 60, 90, 50);
    }
}
