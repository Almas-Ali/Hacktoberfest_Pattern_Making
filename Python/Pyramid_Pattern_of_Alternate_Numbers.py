# Pyramid Pattern of Alternate Numbers

def pypattern(rows):

    i = 1

    while i <= rows:

        j = 1

        while j <= i:

            print(((i * 2) - 1), end=" ")

            j = j + 1

        i = i + 1

        print()

# Driver Code
rows = 5
pypattern(rows)