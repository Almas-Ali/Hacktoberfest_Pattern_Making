# Function to print the pattern of a fish over N rows
def printFish(N) :

	spaces = "";
	char1 = "F"; char2 = "";
	for i in range(N) :
		spaces += ' ';

	for i in range( 2 * N + 1) : # first N for upper part, then second N for lower part, and +1 for middle part
		# For upper part
		if (i < N) :
			print(spaces,end="");
			print(char1,end="");
			print(spaces,end="");
			print(spaces,end="");
			print(char2);
			spaces = spaces[:-1]
			char1 += "FF";
			char2 += "F";

		# For middle part
		if (i == N) :
			print(spaces,end="");
			print(char1,end="");
			print(spaces,end="");
			print(spaces,end="");
			print(char2);

		# For lower part
		if (i > N) :
			spaces += ' ';
			char1 = char1[:-1];
			char1 = char1[:-1];
			char2 = char2[:-1];
			
			print(spaces,end="");
			print(char1,end="")
			print(spaces,end="");
			print(spaces,end="");
			print(char2);

# Driver Code
if __name__ == "__main__" :

	N = 4;
	printFish(N);