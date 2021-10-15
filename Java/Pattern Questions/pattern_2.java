//Question no: 2


package com.java;

public class patternQns2 {
    public static void main(String[] args) {
        int n = 5;
        Answer(n);
    }

    static void Answer(int n) {
        for (int row = 1; row <= n ; row++) {
            for (int col = 1; col <= n ; col++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}

//Output
//*****
//*****
//*****
//*****
//*****
