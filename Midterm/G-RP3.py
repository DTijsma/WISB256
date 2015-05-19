data=input()

data=data.split(' ')
data2=data.copy()
def f(a,b,c):
    
    if c=='+':
        return (a + '+' + b)
    elif c=='-':
        return (a + '+' + b)
    elif c=='*':
        return (a + '+' + b)
    elif c=='/':
        return (a + '+' + b)

def g(a,b,c):
    if c=='+':
        return a + ' + ' + b
    elif c=='-':
        return '(' + a + ')' + ' - '+ '(' + b + ')'
    elif c=='*':
        return '(' + a + ')' + ' * '+ '(' + b + ')'
    elif c=='/':
        return '(' + a + ')' + ' / '+ '(' + b + ')'

getallen="0,1,2,3,4,5,6,7,8,9".split(',')
operaties=['+','-','*','/']

#print(data)
mlijst=[]
lijstje2=[]
#while data[1]!=2:
#    binlijst=[0]*len(data)
#    for i in range(len(data)):
#        if data[i] in operaties:
#            binlijst[i]=1
#    
#    lijstje=[]
#    for t in range(len(binlijst)-2):
#        if binlijst[t]==0 and binlijst[t+1]==0 and binlijst[t+2]==1:
#            lijstje.append(t)
#    m=min(lijstje)
#    mlijst.append(m)
#    lijstje2.append(data[m])
#    lijstje2.append(data[m+1])
#    lijstje2.append(data[m+2])
#    
#    data[m]=f(data[m],data[m+1],data[m+2])
#    for i in range(m+1,len(data)-2):
#        data[i]=data[i+2]
#    data[-1]=2
#    data[-2]=2
            
while data[1]!=2:
    binlijst=[0]*len(data)
    for i in range(len(data)):
        if data[i] in operaties:
            binlijst[i]=1
    
    lijstje=[]
    for t in range(len(binlijst)-2):
        if binlijst[t]==0 and binlijst[t+1]==0 and binlijst[t+2]==1:
            lijstje.append(t)
    m=min(lijstje)
    mlijst.append(m)
    lijstje2.append(data[m])
    lijstje2.append(data[m+1])
    lijstje2.append(data[m+2])
    
    data[m]=g(data[m],data[m+1],data[m+2])
    for i in range(m+1,len(data)-2):
        data[i]=data[i+2]
    data[-1]=2
    data[-2]=2
    
#print(lijstje2)
#print(mlijst)
print(data[0])
print(len(data[0]))

aapje=[0]*len(data[0])
for i in range(len(data[0])):
    if data[0][i]=='(' or data[0][i]==')':
        aapje[i]=1

lijstje=[]
qwerty=0

while qwerty!=1:
    for t in range(len(aapje)-2):
        if aapje[t]==1 and aapje[t+1]==0 and aapje[t+2]==0:
            lijstje.append(t)
 
    m=min(lijstje)
    if m==[]:
        qwerty=1
    

print(aapje)
#   5 1 2 + 4 * + 3 -