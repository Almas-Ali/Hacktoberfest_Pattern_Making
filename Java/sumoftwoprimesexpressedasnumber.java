import java.util.*;
public class sumoftwoprimesequalstonumber {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int num,i;
        boolean flag=true;
        num=sc.nextInt();
        for(i=2;i<num/2;i++){
            if(isprime(i)){
            if(isprime(num-i)){
        System.out.println("Given Number  "+ num +" is Expressed in sum of primes of "+ i +" and "+(num-i));
        flag=false;
            }}
        }
        if(flag){
            System.out.println(num + " cannot be expressed as the sum of two prime numbers.");
        }
    }
        public static boolean isprime(int n){
            boolean prime=true;
        for(int i=2;i<=n/2;i++){
            if(n%i==0){        
            prime=false;
            break;
            }
        }
        return prime;
    }
}