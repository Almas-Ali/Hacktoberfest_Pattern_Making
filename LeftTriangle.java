import java.io.*;

// java program for left triangle
public class GFG {
	// Function to demonstrate printing pattern
	public static void StarleftTriangle(int k)
	{
		int a, b;

		// 1st loop
		for (a = 0; a < k; a++) {

			// nested 2nd loop
			for (b = 2 * (k - a); b >= 0; b--) {
				// printing spaces
				System.out.print(" ");
			}

			// nested 3rd loop
			for (b = 0; b <= a; b++) {
				// printing stars
				System.out.print("* ");
			}

			// end-line
			System.out.println();
		}
	}

	// Driver Function
	public static void main(String args[])
	{
		int k = 5;
		StarleftTriangle(k);
	}
}
