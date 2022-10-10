s = input()
d = {}
for i in s:
  if i == " ":
    continue
  d[i] = d.get(i,0)+1
print(d)


# contributed by anuragshuklajec
# The dictionary prints frequency of every character
