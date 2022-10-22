public class Pattern31 {
    public static void main(String[] args) {
        pattern31(5);
    }
static void pattern31(int n) {
        int originalN = n;
        n = n * 2;
        for (int row = 1; row < n; row++) {
            for (int col = 1; col < n; col++) {
                int atEveryIndex = originalN - Math.min(Math.min(row, col), Math.min(n - row, n - col));
                System.out.print(atEveryIndex + 1 + "  ");
            }
            System.out.println();
        }
    }
}
