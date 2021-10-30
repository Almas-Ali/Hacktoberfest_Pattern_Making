print(f'Enter the range of numbers you want to check if they are prime.')
min = int(input(f'first number: '))
max = int(input(f'last number: '))

for num in range(min,max):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
        print (num)
