def gcd(x, y):
    if (y == 0):
        return x
    elif(x >= y and y > 0):
        # x greater than y
        return gcd(y, x % y)
    else:
        return gcd(x,(y % x))


a = int(input("Enter 1st no.  "))
b = int(input("Enter 2nd no.  "))
print(gcd(a, b))
