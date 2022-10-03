import re
for n in range(int(input())):
    pattr=re.compile(r'(?<!^)(#(?:[\da-f]{3}){1,2})',flags=re.I)
    for x in pattr.findall(input()):
        print(x)