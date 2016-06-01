public class Test {
    public static void main(String...args) {
        Sfmt sfmt = new Sfmt(0);

        for (int a = 0; a < 100; a++) {
            System.out.println(sfmt.NextInt(1000) + " ");
        }
    }
}
