# Challenge by Hima in C language
# Write a program that returns the next largest number that can be created from the
# same digits as the input.
# Examples--
# next_number(19) ➞ 91
# next_number(3542) ➞ 4235
# next_number(5432) ➞ 5432
# next_number(58943) ➞ 59348
# Notes--
# If no larger number can be formed, return the number itself.
num = input("Enter The Number")
num2 = list(num)
num2.sort()
num2.reverse()
num3 = str(num2)
print(num3)
