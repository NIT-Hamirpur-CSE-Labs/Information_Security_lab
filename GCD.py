def gcd(x,y):
    if(y==0):
        return x
    elif(x>=y and y>0):
        return gcd(y,(x % y))
    else:
        return gcd(x,(y % x))


a = int(raw_input("enter 1st no.  "))
b = int(raw_input("enter 2nd no.  "))
print gcd(a,b)
