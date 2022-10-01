def staircase(n, s = ""):
    c = "_#"
    if n != 0:
        if len(s) // abs(n) >= abs(n):
            return s
        a = abs(n) - (len(s) // abs(n)) - 1
        b = len(s) // abs(n) + 1
        s += f"{c[0]*(a if n > 0 else b-1)}{c[1]*(b if n > 0 else a+1)}" + ("\n" if len(s) // abs(n) < abs(n) else "")
        return staircase(n, s)
    return "Not Draw!"
    
print(staircase(int(input("Enter Input : "))))