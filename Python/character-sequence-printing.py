#This code is provided by codebyAbhishekBharti
#This will print the code like given below
#A 
#B C 
#D E F 
#G H I J 
#K L M N O 
#P Q R S T U 
#V W X Y Z [ \ 


n=7
count=65
x=0
for i in range(1,n+1):
	for j in range(1,i+1):
		print(chr(count+x),end=' ')
		x+=1
	print()
