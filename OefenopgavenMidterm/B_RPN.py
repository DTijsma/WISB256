data=input()

data2=data.split(' ')

data2[0]=int(data2[0])
data2[1]=int(data2[1])

if data2[2]=='+':
    print("{0:.3f}".format(data2[0]+data2[1]))
elif data2[2]=='-':
    print("{0:.3f}".format(data2[0]-data2[1]))
elif data2[2]=='*':
    print("{0:.3f}".format(data2[0]*data2[1]))
elif data2[2]=='/':
    print("{0:.3f}".format(data2[0]/data2[1]))
elif data2[2]=='**':
    print("{0:.3f}".format(data2[0]**data2[1]))