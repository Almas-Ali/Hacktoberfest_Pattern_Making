# output:
# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1 

# PROGRAM:

# first we take no. of rows
rows = 6

for i in range(1, rows):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print("")