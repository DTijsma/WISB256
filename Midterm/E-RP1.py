data=input()

data=data.split(' ')

def f(a,b,c):
    
    if c=='+':
        return float(a)+float(b)
    elif c=='-':
        return float(a)-float(b)
    elif c=='*':
        return float(a)*float(b)
    elif c=='/':
        return float(a)/float(b)


getallen="0,1,2,3,4,5,6,7,8,9".split(',')
operaties=['+','-','*','/']

#print(data)

while data[1]!=2:
    binlijst=[0]*len(data)
    for i in range(len(data)):
        if data[i] in operaties:
            binlijst[i]=1
    
    #print(binlijst)
    
    lijstje=[]
    for t in range(len(binlijst)-2):
        if binlijst[t]==0 and binlijst[t+1]==0 and binlijst[t+2]==1:
            lijstje.append(t)
    m=min(lijstje)
    
    data[m]=f(data[m],data[m+1],data[m+2])
    for i in range(m+1,len(data)-2):
        data[i]=data[i+2]
    data[-1]=2
    data[-2]=2
    
    #print(data)
            


print("{0:.3f}".format(data[0]))