fhand=open('sample.txt')
inp=fhand.read()
#print(inp)
lis=list(inp)
#print(lis)
inp=''
for i in lis:
    if i=='\n':
        lis.remove('\n')
for i in lis:
    inp+=i
fhand2=open('sample.txt','w')
fhand2.write(inp)
fhand2.close()
