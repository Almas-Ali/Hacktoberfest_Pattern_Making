package hacktoberfest;
import java.util.Scanner;

public class NumberPattern {
            
	    public static void main(String[] args) 
	    {
	        Scanner sc = new Scanner(System.in); //Taking rows value from the user    
	        System.out.println("Enter the number of rows to be printed: ");    
	        int rows = sc.nextInt();         
	        for (int i = 1; i <= rows; i++) 
	        {
	            for (int j = 1; j <= i; j++)
	            {
	                System.out.print(i+" ");
	            }
	               
	            System.out.println();
	        }         
	        sc.close();
	    }
	}