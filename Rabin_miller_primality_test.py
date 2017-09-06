import random
#Algorithm
#It returns false if n is composite and true if n is probably prime. K is an input parameter that determines accuracy level.
#Higher valur of k indicates more accuracy.

#miller test algo
def millertest(d,n):
   #pick random no. in [2...n-2] and make sure its >4
   a = 2 + random.randint(1,100000) % (n-4)
   #Compute a^d % n
   x = (a**d) % n
   if(x == 1 or x == n-1):
       return True

   while(d != n-1):
       x = (x*x) %n
       d *= 2
       if(x == 1):
           return False
       if(x == n-1):
           return True

   return False

#checking if prime
def isprime(n,k):
    #corner cases
    if(n<=1 or n==4):
        return False
    if(n<=3):
        return True

    # Find r such that n = 2^d * r + 1 for some r >= 1
    d = n-1
    while(d%2 == 0):
        d/=2
        
    #Iterate given no. k times
    for i in range(0,k):
        if(millertest(d,n) == False):
            return False
        #return False

    return True

#main program
k = 4   #no. of iterations
print"All prime no.'s b/w 0 - 100"
for n in range(1,100):
    if(isprime(n,k)):
        print n
