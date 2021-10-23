package hacktoberfest;

import java.util.Scanner;

public class CheckAutomorphicNumber {

	public static void main(String args[]) {

		// Get number as input
		Scanner in = new Scanner(System.in);
		System.out.println("Enter a number");
		int input = in.nextInt();

		// Checking AutomorphicNumber or not
		boolean isAutomorphicNumber = isAutomorphicNumber(input);
		// Printing result
		if (isAutomorphicNumber) {
			System.out.println(input + " is automorphic number");
		} else {
			System.out.println(input + " is not automorphic number");
		}
	}

	// Method to verify Automorphic number
	private static boolean isAutomorphicNumber(int number) {
		int noOfDigits = 0;
		int sqrOfN = number * number;
		System.out.println("Square of input number is: " + sqrOfN);
		int temp = number;

		// count digits of number
		while (temp > 0) {
			noOfDigits++;
			temp = temp / 10;
		}

		int lastNDigitsOfSquare = (int) (sqrOfN % (Math.pow(10, noOfDigits)));

		if (number == lastNDigitsOfSquare)
			return true;
		else
			return false;
	}
}
