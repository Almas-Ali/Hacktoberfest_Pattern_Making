def pascalTriangle(size):
    for i in range(0,size):
        for j in range(0, i + 1):
            print(binomial(i,j),end = " ")
        print()

def binomial(n,k):
    res = 1
    if (k > n-k):
        k = n-k
    for i in range(0,k):
        res = res * (n-i)
        res = res // (i+1)
    return res

if __name__ == "__main__":
    pascalTriangle(5)
