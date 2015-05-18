smax=int(input())
tabel=input()

aantal=0
people=int(tabel[0])

for i in range(1,1+smax):
    if people<i and int(tabel[i])>0:
        aantal=aantal+i-people
        people=i+int(tabel[i])
    else:
        people=people+int(tabel[i])

print(aantal)
    