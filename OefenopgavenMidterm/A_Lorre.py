n=int(input())

lijst=[]
for i in range(n):
    lijst.append(i)

for i in range(n):
    lijst[i]=input()

for i in range(n):
    if len(lijst[i].split(' '))>4:
        print('Crackers!')
    else:
        print(lijst[i], 'krAh!')
