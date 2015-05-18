n=int(input())

lijst=[]
for i in range(n):
    lijst.append(i)

for i in range(n):
    lijst[i]=input()

dobbel=[6,4,2]

for i in range(len(lijst)):
    
    if lijst[i]=='omhoog':
        a=dobbel[0]
        b=dobbel[1]
        c=dobbel[2]
        
        dobbel[0]=b
        dobbel[1]=7-a
    
    if lijst[i]=='omlaag':
        a=dobbel[0]
        b=dobbel[1]
        c=dobbel[2]
        
        dobbel[0]=7-b
        dobbel[1]=a
    
    if lijst[i]=='links':
        a=dobbel[0]
        b=dobbel[1]
        c=dobbel[2]
        
        dobbel[0]=7-c
        dobbel[2]=a
    
    if lijst[i]=='rechts':
        a=dobbel[0]
        b=dobbel[1]
        c=dobbel[2]
        
        dobbel[0]=c
        dobbel[2]=7-a
    

print(dobbel[0])