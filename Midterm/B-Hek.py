n=int(input())

lijst=[]
for i in range(n):
    lijst.append(i)

for i in range(n):
    lijst[i]=input()

som=0
for i in range(n):
    for j in range(len(lijst[i])):
        if lijst[i][j]=='#':
            som=som+1

print('Om de hekjes in dit weiland te verven heb je', som*5, 'liter verf nodig')