k=int(input())

lijstk=[]
for i in range(k):
    lijstk.append(i)

for i in range(k):
    lijstk[i]=input()

n=int(input())

lijstn=[]
for j in range(n):
    lijstn.append(j)

for j in range(n):
    lijstn[j]=input()
    

print(lijstk)
print(lijstn)

for i in range(n):
    eerste=lijstn[i][0]
    laatste=lijstn[i][-1]
    for j in range(k):
        if lijstk[j][0]==eerste and lijstk[j][-1]==laatste:
            for m in range(1,len(lijstk[j])-1):  #Letter uit ytho zoeken.
                
                lijstje=[]
                for t in range(len(lijstn[i])): #In poiuytghjiokn
                    if lijstn[i][t]==lijstk[j][m]:
                        lijstje.append(t)
                
                if lijstje==[]:
                     '?'
                else:
                    cursor=min(lijstje)

                


#for i in range(n):
#    eerste=lijstn[i][0]
#    laatste=lijstn[i][-1]
#    for j in range(k):
#        if lijstk[j][0]==eerste:
#            if lijstk[j][-1]==laatste:
#                cursor=0
#                for m in range(1,len(lijstn[i])):
#                    for t in range(1,len(lijstk[j])):
#                        lijstje=[]
#                        if lijstk[j][t]==lijstn[i][m]:
#                            lijstje.append(t)
#                        cursor=min(lijstje)
#                
#                
#                print('Hoi.')
#            else:
#                print('?')
#        else:
#            print('?')


#alfabet="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(',')
#print(alfabet)

