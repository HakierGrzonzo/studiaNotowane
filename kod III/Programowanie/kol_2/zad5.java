// zadanie 5
import java.io.*;
import java.util.*;
class Main {
    public static void main(String[] args) {
        System.out.println(new Punkt3DKolor(
                    2, 1, 37, 
                    new Kolor((byte) 1, (byte) 255, (byte) -1) // -1 zamieni się w 255
                )
            );
    }
}

class Punkt2D {
    public double x;
    public double y;
    public Punkt2D(double x, double y) {
        this.x = x;
        this.y = y;
    }
}

class Punkt3D extends Punkt2D {
    public double z;
    public Punkt3D(double x, double y, double z) {
        super(x, y);
        this.z = z;
    }
    public String toString() {
        return "<Punkt3D: " + x + "; " 
            + y + "; "
            + z + ">";
    }
}

class Kolor {
    public byte r;
    public byte g;
    public byte b;
    public Kolor(byte r, byte g, byte b) {
        this.r = r;
        this.g = g;
        this.b = b;
    }
    public String toString() {
        return "<Kolor: " + Byte.toUnsignedInt(r) + ", " 
            + Byte.toUnsignedInt(g) + ", "
            + Byte.toUnsignedInt(b) + ">";
    }
}

class Punkt3DKolor extends Punkt3D {
    public Kolor kolor;
    public Punkt3DKolor(double x, double y, double z, Kolor kolor) {
        super(x, y, z);
        this.kolor = kolor;
    }
    @Override
    public String toString() {
        return "<Punkt3DKolor: " + x + "; " 
            + y + "; "
            + z + ">\n\t" + kolor + "\n</Punkt3DKolor>";
    }
}
