import sys
import math

data=open(sys.argv[1], "r")

C=0.6601618

primelist=[]
for line in data:
    primelist.append(int(line.replace('\n', '')))

data.close()

piN=len(primelist)
largestprime=primelist[piN-1]
ratio=piN*(math.log(largestprime))/largestprime

k=1
piN2=0
while k<piN:
    if primelist[k]-primelist[k-1]==2:
        piN2+=1
    k+=1

print('Largest Prime = ', largestprime)
print('--------------------------------')
print('pi(N)         = ', piN )
print('N/log(N)      = ', largestprime/(math.log(largestprime)) )
print('ratio         = ', ratio )
print('--------------------------------')
print('pi_2(N)       = ', piN2 )
print('2CN/log(N)^2  = ', 2*C*largestprime/(math.log(largestprime))**2 )
print('ratio         = ', piN2*((math.log(largestprime))**2)/(2*C*largestprime) )
print('--------------------------------')

