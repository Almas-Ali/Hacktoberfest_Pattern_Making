// Created by Fluxyl on GitHub
import java.util.Scanner;

public class UltraPattern {
	public static void main(String[] args) {
		
		System.out.println("rows: ");
		Scanner scanner = new Scanner(System.in);
		
	    int rows = scanner.nextInt();
		
		System.out.println("symbol: ");
		String strSymbol = scanner.next();
		
		int columns = rows - 1;
		int i, j = 1;
		for (j = 1; j <= rows; j++) {			
			columns =- 1;
			for (i = 1; i <= 4 * j - 4; i++) {  
				System.out.print(strSymbol);
			}
			System.out.println("?");
		}
				  
		columns = 1;  
		for (j = 1; j <= rows - 1; j++) {  
			for (i = 1; i <= columns; i++){  
				System.out.print(strSymbol);  
			}
			columns =+ 1;  
			for (i = 1; i <= 3 * (rows - j) - 1 + 23; i++){  
				System.out.print(strSymbol);  
			}  
			System.out.println("!");
		}
	}
}
		
