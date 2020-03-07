#This only when user gives the input...
#This can be implemented for random numbers also.
nums=[]
while True:                                   #loop2
    num = input("Enter Number:- ")
    if num.isnumeric():
        nums.append(int(num))
    elif num == 'done':
        break
print(nums)
#min=nums[0]
for1count=0        #counter for for loop...but it always needs len(nums)-1 iterations.
whilecount=0        #counter for while loop
while whilecount<len(nums):
    for i in range(whilecount,len(nums)):
        if nums[whilecount]>nums[i]:
            #min=nums[i]
            nums[i],nums[whilecount]=nums[whilecount],nums[i]
            print(nums)
        for1count+=1
    whilecount+=1
#print('Lowest is',min)                #minimum number in the whole list
print('for loop count',for1count)
print('length',len(nums))
print('whilecount',whilecount)
print(nums)
