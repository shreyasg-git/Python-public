
print('=================Part 1===========================')
fhand=open('mbox-short.txt')
print(fhand)
print('=================Part 2===========================')
count=0
for line in fhand:
    count+=1
print(count)
print('=================Part 3============================')
inp=fhand.read()
print(len(inp))
print(inp[:2])
