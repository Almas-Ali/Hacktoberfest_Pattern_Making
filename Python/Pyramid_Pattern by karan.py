def pyramid_pattern(n):
    for i in range(0, n):
        
        for j in range(0, i+1):
            
            print("* ",end="")
            
        print("\r")
n= int(input("Enter the integer value: "))
pyramid_pattern(n)
