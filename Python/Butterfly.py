''' 

*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 

'''


n = int(input("Enter the number: "))

for i in range(1,(n+1)):
  for j in range(0,i):
    print("*", end = ' ')
  space = 2*n - 2*i
  for k in range(0,space):
    print(" ",end=' ')
  for m in range(0,i):
    print("*", end =' ')
  print()
  
for i in range(n,0,-1):
  for j in range(0,i):
    print("*", end = ' ')
  space = 2*n - 2*i
  for k in range(0,space):
    print(" ",end=' ')
  for m in range(0,i):
    print("*", end =' ')
  print()
