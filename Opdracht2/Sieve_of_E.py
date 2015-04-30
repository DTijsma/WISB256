import time
import math
import sys

#print('Number of arguments:', len(sys.argv), 'arguments.')
#print('Argument List:', str(sys.argv))

N=int(sys.argv[1])
#N=int(input('Give a natural number. '))

start = time.time()

#output=open('output.txt', 'w')
output=open(sys.argv[2], 'w')

lijst=[]
for i in range(N):
    lijst.append(1)

m=1
while m<int(math.sqrt(N)):
    if lijst[m]==1:
        for k in range(1,int(N/(m+1))):
            lijst[(m+1)*k+m]=0
    m+=1

primelist=[]
for k in range(1,N):
    if lijst[k]==1:
        primelist.append(k+1)

for item in primelist:
    output.write("%s\n" % item)

output.close()

end = time.time()

#print(primelist)
print('Found', len(primelist) , 'Prime numbers smaller than' , sys.argv[1] , 'in' ,  end-start , 'seconds.')
print('--------------------------------------------------------------------------------')
#print(end-start)