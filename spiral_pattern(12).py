# complete
# 4 hours approx.
# 23/03/2020
n = int(input('Enter The Side Of The Square : '))


def createarray(side):         # creates matrix nxn.
    matrix = [[0 for row in range(side)] for column in range(side)]
    return matrix


arr1 = createarray(n)
# building dir starts here.
direction = ['K']       # dir is the direction's list acc to which the matrix changes
nums = []
for t in range(3):
    nums.append(n-1)
z = n-2
for t in range(n-2):
    if z >= 1:
        nums.append(z)
        nums.append(z)
    z -= 1
dirs = []
dirsamples = ['R', 'D', 'L', 'U']  # this is order in which directions changes

for t in range(2*n):
    dirs = dirs+dirsamples
dirs = dirs[:n*n]
k = 0

for t in range(0, len(nums)):
    for x in range(nums[k]):
        direction.append(dirs[t])
    k += 1
direction.append('K')
# building dir ends here
# print(dir)
del k, z
i = 0
j = 0

for x in range(1, len(direction)):
    arr1[i][j] = x
    if direction[x] == 'R':
        j += 1
    elif direction[x] == 'D':
        i += 1
    elif direction[x] == 'L':
        j -= 1
    elif direction[x] == 'U':
        i -= 1
for i in range(n):  # just to print
    print(arr1[i])
print('-------')
