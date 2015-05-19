N=int(input())

lijstje=[0,0,0,1]

for i in range(N):
    lijstje.append(lijstje[-1]+lijstje[-2]+lijstje[-3]+lijstje[-4])
    
    
print(lijstje[N])
