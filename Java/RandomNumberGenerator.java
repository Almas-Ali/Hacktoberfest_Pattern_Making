import java.util.*;
import java.lang.*;
import java.io.*;
import java.lang.Math;  

class RandomNumberGenerator  {  
    public static void main( String args[] ) {  
    	int left = 1;  
    	int right = 100;  
    	//Generate random value from 1 to 100   
    	System.out.println("Random value of type double between "+left+" to "+right+ ":");  
    	int thisIsARandomNumber = (int)(Math.random()*(right-left+1)+left);   
    	System.out.println(thisIsARandomNumber);  
    }  
} 
