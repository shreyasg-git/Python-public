main = 21
print("The no. of match sticks is 21 now.")
choice1 = int(input("Enter The number of matchsticks u wanna reduce : "))
if choice1 in range(1, 5):
    print("No. of matchsticks is = ", main-choice1)
    print("I Chose               = ", main-choice1-16)
    print("Hence No. Of matchsticks is = ", 16)
else:
    print("Invalid Move !")
choice2 = int(input("Enter your Choice : "))
if choice2 in range(1, 5):
    print("No. of matchsticks is = ", 16-choice2)
    print("I Chose =               ", 16-choice2-11)
    print("Hence No. Of matchsticks is = ", 11)
else:
    print("Invalid Move !")
choice3 = int(input("Enter Your Choice : "))
if choice3 in range(1, 5):
    print("No. of matchsticks is = ", 11-choice3)
    print("I Chose               = ", 11-choice3-6)
    print("Hence No. Of matchsticks is = ", 6)
else:
    print("Invalid Move !")
choice4 = int(input("Enter Your Choice : "))
if choice4 in range(1, 5):
    print("No. of matchsticks is = ", 6-choice4)
    print("I Chose               = ", 6-choice4-1)
    print("Hence No. Of matchsticks is = ", 1)
else:
    print("Invalid Move !")
print("You Lose !!!!!")
