n = int(input())

space = n-1
inSpace = 1
for i in range(0,n):
    for sp in range(space):
        print(" ",end='')
    print('*',end="")
    if i != 0:
        for sp in range(inSpace):
            print(" ",end='')
        print('*',end="")
        inSpace += 2
    space -=1    
    print()

space += 2
inSpace -= 4

for i in range(n-1):
    for sp in range(space):
        print(" ",end='')
    print('*',end="")
    if i != n-2:
        for sp in range(inSpace):
            print(" ",end='')
        print('*',end="")
        inSpace -= 2
    space +=1    
    print()
