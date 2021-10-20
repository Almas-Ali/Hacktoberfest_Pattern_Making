

import java.util.*;


public class Solution {


   public static void main(String[] args){
       Scanner sc = new Scanner(System.in);

       System.out.println("Enter any Number "); 
       int no = sc.nextInt();

       boolean isPrime = true;
       for(int i = 2; i<=no/2; i++){
           if(no%i==0){
               isPrime = false;
               break;
           }
       }
       if(isPrime){
           if(no == 1){
               System.out.println("This is neither Prime nor Composite");
           }else{
            System.out.println("This is a Prime number ");
           }
       }else{
        System.out.println("This is not a Prime number ");
       }
   }
}
