import java.io.*;
import java.util.*;

class Factorial
{
    public static void main(String args[])throws IOException
    {
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while(t-- > 0)
        {
            int N = Integer.parseInt(read.readLine());
            Solution ob = new Solution();
            System.out.println(ob.factorial(N));
        }
    }
}


class Solution{
    static long factorial(int N){
        // code here
        if(N==0) return 1;
        
        return N*factorial(N-1);
    }
}
