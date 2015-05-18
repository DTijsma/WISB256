message=input()
codeword=input()

lijst=[]

for i in range(len(message)):
    x=ord(codeword[i%len(codeword)])-96
    z=ord(message[i])-96
    a=(z-x+1)%26
    if a==0:
        a=26
    a=int(a+96)
    lijst.append(chr(a))

bericht=''
for letter in lijst:
    bericht=bericht+letter

print(bericht)