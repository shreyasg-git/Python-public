##Logic behind no. of iterations of outer loop - think of the worst case
##i.e. the highest number is at the last position...hence it will take 'n' iterations to take it to the first position.
'''from random import randint
n=int(input("Enter the No.of numbers : "))
m=int(input("Enter The range of numbers : "))
num=[]
for x in range(0,n):
    num.append(randint(1,m))'''

try:
    print("type 'stop' when done  !")
    num=[]
    while True:
        num.append(int(input()))
except:
    print("_ended_here_")

for times in range(1,len(num)):
    for n in range(1,len(num)-times+1):
        if num[n]>num[n-1]:
            num[n],num[n-1]=num[n-1],num[n]
    print(num)
print(num)
#Take trials on---
'''345
6346
346
453
45
3423
34343'''
