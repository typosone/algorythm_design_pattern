public class Count {
    public static void main(String...args) {
        Sfmt sfmt = new Sfmt(256);
        for (int a = 0; a < 10; a++) {
            byte b = (byte)sfmt.NextInt(256);
            int c = Integer.bitCount(b);
            System.out.printf("%4d の1の個数: %d\n", b, c);
        }
    }
}
