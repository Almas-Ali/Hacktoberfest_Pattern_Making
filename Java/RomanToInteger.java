package hacktoberfest;

import java.util.*;

class RomanToInteger {

	public static int romanToInteger(String roman) {
		Map<Character, Integer> numbersMap = new HashMap<>();
		numbersMap.put('I', 1);
		numbersMap.put('V', 5);
		numbersMap.put('X', 10);
		numbersMap.put('L', 50);
		numbersMap.put('C', 100);
		numbersMap.put('D', 500);
		numbersMap.put('M', 1000);

		int result = 0;

		for (int i = 0; i < roman.length(); i++) {
			char ch = roman.charAt(i); // Current Roman Character

			
			if (i > 0 && numbersMap.get(ch) > numbersMap.get(roman.charAt(i - 1))) {
				result += numbersMap.get(ch) - 2 * numbersMap.get(roman.charAt(i - 1));
			}

			
			else
				result += numbersMap.get(ch);
		}

		return result;
	}

	public static void main(String args[]) {
		// Take input as a String
		String romanNumber = "MCCXCIV";
		int result = romanToInteger(romanNumber);

		System.out.println("The Roman Number is: " + romanNumber);
		System.out.println("Its Integer Value is: " + result);
	}

}
