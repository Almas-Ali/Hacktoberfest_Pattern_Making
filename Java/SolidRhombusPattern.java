

public class Solidrhombus {
    public Solidrhombus() {
    }

    public static void main(String[] args) {
        int n = 5;

        for(int i = 1; i <= n; ++i) {
            int j;
            for(j = 1; j <= n - i; ++j) {
                System.out.print(" ");
            }

            for(j = 1; j <= 5; ++j) {
                System.out.print("*");
            }

            System.out.println();
        }

    }
}
