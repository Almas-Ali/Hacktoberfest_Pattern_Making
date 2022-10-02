public class heartPattern {
    public static void main(String[] args) {
        int n = 6;
        for (int y = -n; y <= 2 * n; y++) {
            for (int x = -2 * n; x <= 2 * n; x++)
                if ((y <= 0 &&
                        ((int) Math.sqrt((x+n)*(x+n) + y*y) <= n
                                || (int) Math.sqrt((x-n)*(x-n) + y*y) <= n))
                        || (y > 0 && Math.abs(x) <= 2 * n - y))
                    System.out.print("♥ ");
                else
                    System.out.print("♡ ");
            System.out.println();
        }
    }
}
