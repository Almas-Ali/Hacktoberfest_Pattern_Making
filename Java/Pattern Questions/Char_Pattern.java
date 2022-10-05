public class Main {
    public static void main(String[] args) {
        Pattern14(5);
        Pattern18();
    }

    static void Pattern14(int n) {
        for (int i = 1; i <= n; i++) {
            int p = 1;
            for (int j = i; j <= n; j++) {
                System.out.print("  ");
            }
            for (int k = 1; k < i; k++) {
                System.out.print(p++ + " ");
            }
            for (int l = 1; l <= i; l++) {
                System.out.print(p-- + " ");
            }
            System.out.println();
        }

        // 1
        // 1 2 1
        // 1 2 3 2 1
        // 1 2 3 4 3 2 1
        // 1 2 3 4 5 4 3 2 1

    }

    static void Pattern18() {
        // Q. Form a pattern with specific word;
        // word : "CODER"

        String w = "CODER";

        for (int i = 1; i <= 5; i++) {
            int p = 0;
            for (int j = 1; j <= i; j++) {
                System.out.print(w.charAt(p++) + " ");
            }
            System.out.println();
        }
        // C
        // C O
        // C O D
        // C O D E
        // C O D E R
    }
}