/* You are given a number n, representing the number of stairs in a staircase.
You are on the 0th step and are required to climb to the top.
In one move, you are allowed to climb 1, 2 or 3 stairs.
You are required to print the number of different paths via which you can climb to the top. 
-Ishan Gupta
*/
import java.util.*;
public class climbstair{
    public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    int n =s.nextInt();
    System.out.println(ways(n));    
    } 

    public static int ways(int n ){
    int [] arr = new int[n+1];
    arr[n]=1;
         for(int i=n-1;i>=0;i--){
             if(i==n-1){
             arr[i]=arr[n];
             }
             else if(i==n-2){
            arr[i]=arr[n]+ arr[n-1];
             }
             else{
          arr[i] = arr[i+1] + arr[i+2] + arr[i+3];
             }

        }
        return arr[0];
    }
}