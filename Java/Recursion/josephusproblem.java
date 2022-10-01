Given the total number of persons n and a number k which indicates that k-1 persons are skipped and kth person is killed in circle in a fixed direction.

The task is to choose the safe place in the circle so that when you perform these operations starting from 1st place in the circle, you are the last one remaining and survive.

Example 1: 
Input:
n = 3 k = 2
Output: 3
Explanation: There are 3 persons so 
skipping 1 person i.e 1st person 2nd 
person will be killed. Thus the safe 
position is 3.

Example 2 : 
Input:
n = 5 k = 3
Output: 4
Explanation: There are 5 persons so 
skipping 2 person i.e 3rd person will 
be killed. Thus the safe position is 4.


import java.util.*;
public class JosephusProblem {
    //N People are in circle from 0 to n-1, we have to kill Kth person. Output is the last person standing.
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        System.out.println(fun(n,k));
    }
    public static int fun(int n, int k) {
        if(n==1)    return 0;
        else
        return (fun(n-1,k) + k)%n;
        //Recursion, T.C is O(n) and S.C. is also O(n)
    }  
}
