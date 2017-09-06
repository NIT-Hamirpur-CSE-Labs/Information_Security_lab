from numpy.polynomial import polynomial as p
def gcd1(c1,c2):
	if(c1[1:]==0.):
		return c2;
	else:
		division=p.polydiv(c2,c1);
		return (division[1:],c2);


c1=(1,2,3);      
c2=(3,2,1);
#print p.polydiv(c2,c1);
#division=p.polydiv(c2,c1);
#print p.polydiv(c1,c2);
#print division[1:];
#print p.polydiv(c1,c1);
result=gcd1(c2,c1);
print result[0:1];




#print remaider;
