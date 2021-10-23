def PascalTriangle(numRows):
    if numRows == 0:
        return []

    l = []

    l.append([1])
    if numRows == 1:
        return l

    l.append([1, 1])
    for i in range(3, numRows+1):

        row = [0]*i

        row[0] = 1
        row[-1] = 1

        prev = l[-1]

        for j in range(1, i-1):
            row[j] = prev[j-1] + prev[j]

        l.append(row)

    return l


# Driver Code
n = 5
l = PascalTriangle(n)
for row in l:
    numbers = row
    for j in numbers:
        print(j, end=" ")

    print("")
