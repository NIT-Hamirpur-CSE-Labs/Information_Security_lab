def extendedEuclideanGF2(a,b): # extended euclidean. a,b are values 10110011... in integer form
    inita,initb=a,b;  x,prevx=0,1;  y,prevy = 1,0
    while b != 0:
        q = int("{0:b}".format(a//b),2)
        a,b = b,int("{0:b}".format(a%b),2);
        x,prevx = (int("{0:b}".format(prevx-q*x)), int("{0:b}".format(x,2)));  y,prevy=(prevy-q*y, y)
    print("Euclidean  %d * %d + %d * %d = %d" % (inita,prevx,initb,prevy,a))
    return a,prevx,prevy  # returns gcd of (a,b), and factors s and t

def modular_inverse(a,mod): # a,mod are integer values of 101010111... form
    a,mod = prepBinary(a,mod)
    bitsa = int("{0:b}".format(a),2); bitsb = int("{0:b}".format(mod),2)
    #return bitsa,bitsb,type(bitsa),type(bitsb),a,mod,type(a),type(mod)
    gcd,s,t = extendedEuclideanGF2(a,mod); s = int("{0:b}".format(s))
    initmi = s%mod; mi = int("{0:b}".format(initmi))
    print ("M Inverse %d * %d mod %d = 1"%(a,initmi,mod))
    if gcd !=1: return mi,False

    return mi   # returns modular inverse of a,mod

a = raw_input("enter a number ")
mo = raw_input("enter a mod ")

inv = modular_inverse(a,mo)
print inv
