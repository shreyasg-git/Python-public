# code by Shreyas Gangurde
# code for insertion sort using Python
inp=input("Enter The Numbers Separayed by Spaces")
inp=inp.split()
for i in range(len(inp)):
    inp[i]=int(inp[i])
print(inp)
forcnt=0        #just a counter for analyzing
whilecnt=0      #just a counter for analyzing
for x in range(1,len(inp)):
    while inp[x]<inp[x-1] and x-1>=0:
        inp[x],inp[x-1]=inp[x-1],inp[x]
        x-=1
        print(inp)
        whilecnt+=1
    forcnt+=1
print('forcount',forcnt)
print('whilecnt',whilecnt)
