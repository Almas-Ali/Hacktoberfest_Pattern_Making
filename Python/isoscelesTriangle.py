# by sumopht
h = int(input())
w = 2 * h - 1
for m in range(h - 1):
    # pre-star
    print(" " * (h - (m + 1)), end="")

    # 1st star
    print("*", end="")

    # between star
    print(" " * (2 * m - 1), end="")

    # 2nd star
    if m != 0:
        print("*", end="")

    # new line
    print()
# last line
print("*" * w, end="")
