//Zadanie 5
import javax.swing.*;
import java.awt.*;
import java.awt.image.*;
import javax.imageio.*;
import java.net.URL;
class Main {
    public static void main(String[] args) {
        JFrame frame = new JFrame("test");
        Image img = openImage();
        frame.setDefaultCloseOperation(frame.EXIT_ON_CLOSE);
        frame.getContentPane().add(new OldGraphics(img, frame)).setBackground(Color.YELLOW);
        frame.pack();
        frame.setVisible(true);
    }
    public static Image openImage(){
        try{
            URL url = new URL("https://www.grzegorzkoperwas.site/hakiergrzonzo.png");
            BufferedImage image = ImageIO.read(url);
            return image;

        }
        catch(Exception e){
            e.printStackTrace();
            return null;
        }
    }

}

class OldGraphics extends JPanel {
    private Image img;
    private JFrame frame;
    public OldGraphics(Image img, JFrame frame) {
        this.img = img;
        this.frame = frame;
    }
    public Dimension getPreferrdSize() {
        return new Dimension(200, 200);
    }

    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        for (int x = 0; x < this.frame.getSize().width; x += this.img.getWidth(null)) {
            for (int y = 0; y < this.frame.getSize().height; y += this.img.getHeight(null)) {
                g.drawImage(this.img, x, y, null);
            }
        }
    }
}
