import sys
import math

data=open(sys.argv[1], "r")

C=0.6601618

primelist=[]
for line in data:
    primelist.append(int(line.replace('\n', '')))

data.close()

piN=len(primelist)
lp=primelist[piN-1]
ratio=piN*(math.log(lp))/lp

k=1
piN2=0
while k<piN:
    if primelist[k]-primelist[k-1]==2:
        piN2+=1
    k+=1

logje=math.log(lp)

print('Largest Prime =', lp)
print('----------------------------------')
print('pi(N)         =', piN )
print('N/log(N)      =', lp/(logje) )
print('ratio         =', ratio )
print('----------------------------------')
print('pi_2(N)       =', piN2 )
print('2CN/log(N)^2  =', 2*C*lp/(logje)**2 )
print('ratio         =', piN2*(logje)**2/(2*C*lp) )
print('----------------------------------')

