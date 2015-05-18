
def findRoot(f,a,b,epsilon):
    m=(a+b)/2
    if f(a)==0:
        return a
    elif f(b)==0:
        return b
    elif abs(b-a)<=epsilon:
        return m
    elif f(m)==0:
        return m
    elif f(a)*f(m)<0:
        return findRoot(f,a,m,epsilon)
    elif f(m)*f(b)<0:
        return findRoot(f,m,b,epsilon)


def findAllRoots(f,a,b,epsilon):
    lijstje=[]
    d=abs(b-a)/10000
    for i in range(10000):
        if f(a+d*i)*f(a+d*(i+1))<0:
            nulpunt=findRoot(f,a+d*i,a+(d+1)*i,epsilon)
            lijstje.append(nulpunt)
    
    
    return lijstje
    


