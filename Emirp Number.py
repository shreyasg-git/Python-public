num1=input("Enter The Number")
subject1=list(range(1,int(num1)))
for divisor1 in subject1:
  if int(num1)%divisor1==0:
    original=0
  else:
    original=1
num2=num1[::-1]
subject2=list(range(1,int(num2)))
for divisor2 in subject2:
  if int(num2)%divisor2==0:
    invert=0
  else:
    invert=1
if original==invert:
  print("This is an emirp number \n")
  
