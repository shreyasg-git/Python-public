'''Task:
Create a program to take input a array of numbers and required sum.
Now you have to print the lowest two numbers from the array which sums to the required sum given as input.

Sample :-

input - [10,0,-1,20,25,30]
Required Sum - 45
output - [20,25]'''
#hiiyiyg
def find_match(x,lis):
    n=lis.index(x)
    for m in range(n+1,len(lis)):
        counterforfor2+=1
        if int(lis[m])+int(x)==sum:
            return int(lis[m])
def find_array(lis,sum):
    global counterforfor1=0
    global counterforfor2=0
    for i in lis:
        match=find_match(i,lis)
        counterforfor1+=1
        if match!=None:
            return (int(i),match)
        else:
            return '__NO_combinations_found__'
lis=input('enter the array')
lis=lis.split()
lis.sort()
sum=int(input())
print(find_array(lis,sum))
print('First',counterforfor1,'second',counterforfor2)
