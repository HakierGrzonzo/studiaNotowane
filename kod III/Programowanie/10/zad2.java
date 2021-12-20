//Zadanie 2
import javax.swing.*;
import java.awt.*;
class Main {
    public static void main(String[] args) {
        JFrame frame = new JFrame("test");
        frame.setDefaultCloseOperation(frame.EXIT_ON_CLOSE);
        frame.getContentPane().add(new OldGraphics()).setBackground(Color.YELLOW);
        frame.setVisible(true);
        frame.pack();
    }
}

class OldGraphics extends JPanel {
    public OldGraphics() {

    }
    public Dimension getPreferredSize() {
        return new Dimension(200, 200);
    }

    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.drawOval(10, 10, 150, 150);
        g.drawRect(40, 60, 90, 50);
        g.drawOval(40, 60, 90, 50);
        g.drawLine(40, 60, 40 + 90, 60 + 50);
    }
}
