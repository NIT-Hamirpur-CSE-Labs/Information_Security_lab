#AKS Test to Check if a Given Number is Prime or not.
def expand_x_1(n): 
# This version uses a generator and thus less computations
    c =1
    for i in range(n/2+1):
        c = c*(n-i)/(i+1)
        yield c
 
def aks(p):
    if p==2:
        return True
 
    for i in expand_x_1(p):
        if i % p:
# we stop without computing all possible solutions
            return False
    return True

#main program
print"Enter 2 numbers to find the primes in b/w"
a,b = map(int,raw_input().split())
print"Prime no.'s b/w them are :"
for n in range(a,b):
    if(aks(n)):
        print n
