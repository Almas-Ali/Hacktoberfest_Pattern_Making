a,b=(input().split(" "))
#print(a,b)
c=".|."
for i in range(1,int(a)+1):
    if i==(int(a)+1)//2:
        print("WELCOME".center(int(b),"-"))
    elif i<(int(a)+1)//2:
        j=2*i-1
        print((c*j).center(int(b),"-"))
    else:
        j=2*(int(a)-i)+1
        print((c*j).center(int(b),"-"))
