from string import ascii_lowercase as alpha
size=int(input())
for i in range(size-1,-size,-1):
        temp = '-'.join(alpha[size-1:abs(i):-1]+alpha[abs(i):size])
        print(temp.center(4*size-3,'-'))