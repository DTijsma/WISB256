import sys
import random
import math

if len(sys.argv)<=2 or len(sys.argv)>=5:
    print('Use: estimate_pi.py N L')
elif float(sys.argv[2])<=0:
    print('AssertionError: L should be greater than 0')
else:
    N=int(sys.argv[1])
    L=float(sys.argv[2])
    
    if len(sys.argv)==4:
        random.seed(sys.argv[3])

    def drop_needle(L):
        m=random.random()
        #a=2*3.141592653589793*random.random()
        a=random.vonmisesvariate(0,0)
        if abs(math.ceil(m+L*math.sin(a))-math.ceil(m))>0.1:
            return True
        else: 
            return False
    
    nhits=0
    
    for i in range(N):
        if drop_needle(L)==True:
           nhits+=1
    
    if float(sys.argv[2])<=1:
        pi=2*L*N/(nhits)
    elif float(sys.argv[2])>1:
        pi=2*(math.sqrt(L**2-1)+math.asin(1/L)-L)/(1-nhits/N)
    
    print(nhits , 'hits in', N , 'tries')
    print('Pi =', pi)