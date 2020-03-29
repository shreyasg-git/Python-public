def facto(i):
    # i=int(input("Enter the number"))
    # print('I am calculating facto(',i,')')
    if i == 0:
        return 1
    else:
        return i*facto(i-1)


print(facto(3))
