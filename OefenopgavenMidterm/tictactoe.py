regel1=input()
regel2=input()
regel3=input()

winner=0

if regel1[0]==regel1[1]==regel1[2]:
    if int(regel1[0])>winner:
        winner=int(regel1[0])
if regel2[0]==regel2[1]==regel2[2]:
    if int(regel2[0])>winner:
        winner=int(regel2[0])
if regel3[0]==regel3[1]==regel3[2]:
    if int(regel3[0])>winner:
        winner=int(regel3[0])

if regel1[0]==regel2[0]==regel3[0]:
    if int(regel1[0])>winner:
        winner=int(regel1[0])
if regel1[1]==regel2[1]==regel3[1]:
    if int(regel1[1])>winner:
        winner=int(regel1[1])
if regel1[2]==regel2[2]==regel3[2]:
    if int(regel1[2])>winner:
        winner=int(regel1[2])

if regel1[0]==regel2[1]==regel3[2]:
    if int(regel1[0])>winner:
        winner=int(regel1[0])
if regel1[2]==regel2[1]==regel3[0]:
    if int(regel1[2])>winner:
        winner=int(regel1[2])

if winner>0:
    print('Player', winner, 'wins')
else:
    print('No winner')