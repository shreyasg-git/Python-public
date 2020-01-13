# By Hima in C programmers
# Garland Words
# A Garland word is one that starts and ends with the same N letters in
# the same order, for some N greater than 0, but less than the length of the word.
# N is called the garland word's degree.
# For instance, "onion" is a garland word of degree 2, because its first 2
# letters "on" are the same as its last 2 letters: onion.
# Write a program, that will take a word as input and output
# whether it's a garland word along with the corresponding degree.
name=input("")
n=list(range(1,(len(name)//2)+1))
for length in n:
    if name[0:length]==name[len(name)-length:len(name)]:
        print("This is a Garland word of rank"+str(length))
