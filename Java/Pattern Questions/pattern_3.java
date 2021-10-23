//Question no: 3


package com.java;

public class pattern_3{
    public static void main(String[] args) {
        int n = 5;
        Answer(n);
    }

    static void Answer(int n) {
        for (int row = 0; row < n ; row++) {
            for (int col = 1; col <= (n - row) ; col++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}

// Output
// *****
// ****
// ***
// **
// *

// We Can Also Print This Pattern by this Method

public class star_pattern {

    public static void main(String[] args) {
           int n = 5;
        
        for (int row = 0; row < n; row++) {
            for (int col = row; col < n; col++) {
                System.out.print("* ");

            }
            System.out.println();
        }
// OUTPUT
        
// * * * * * 
// * * * * 
// * * * 
// * * 
// * 
