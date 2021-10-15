import java.util.Scanner;
public class DiamondPattern {
	public static void main(String[] args) {
		
		System.out.println("Enter a number for rows: ");
		Scanner scan = new Scanner(System.in);
		
	    int rows = scan.nextInt();
		
		System.out.println("Enter the symbol for the pattern: ");
		String s = scan.next();
		
		int columns = rows - 1;
		int i, j = 1;
		for (j = 1; j<= rows; j++) {
			for (i = 1; i<= columns; i++) {
				System.out.print(" ");
			}
				
			columns--;
			for (i = 1; i <= 2 * j - 1; i++) {  
				System.out.print(s);
			}
			 
			System.out.println("");
		}
				  
		columns = 1;  
		for (j = 1; j<= rows - 1; j++) {  
			for (i = 1; i<= columns; i++){  
				System.out.print(" ");  
			}  
			columns++;  
			for (i = 1; i<= 2 * (rows - j) - 1; i++){  
				System.out.print(s);  
			}  
			System.out.println("");
		}
	}
}
		