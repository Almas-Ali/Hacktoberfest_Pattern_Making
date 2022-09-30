def pattern(n):

	# Calculating boundary size
	p = 2 * n - 1
	for i in range(1, p + 1):
		for j in range(1, p + 1):

			# Printing the values
			print(max(abs(i - n), abs(j - n)) + 1, " ", end="")
		print()

# Driver code
n = 5
pattern(n)

