def triangle(n):
     
    # number of spaces
    k = n - 1
    
    for i in range(0, n):
     
        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")
     
        # decrementing k after each loop
        k = k - 1
        for j in range(0, i+1):
         
            # printing stars
            print("* ", end="")
        print("\r")
 
# Driver Code
n = 5
triangle(n)
