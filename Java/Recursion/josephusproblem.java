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
