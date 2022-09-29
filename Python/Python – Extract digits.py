from itertools import chain
 
# initializing list
test_list = [(15, 3), (3, 9), (1, 10), (99, 2)]
 
# printing original list
print("The original list is : " + str(test_list))
 
# Extract digits from Tuple list
# Using map() + chain.from_iterable() + set() + loop
temp = map(lambda ele: str(ele), chain.from_iterable(test_list))
res = set()
for sub in temp:
    for ele in sub:
        res.add(ele)
 
# printing result
print("The extracted digits : " + str(res))
