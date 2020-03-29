# Leaders in the list/ array
# Completed and uploaded to GitHub
"""Write a program to print all the LEADERS in the array. An element is leader
if it is greater than all the elements to its right side. And the rightmost element is always a leader.
For example int the array {16, 17, 4, 3, 5, 2}, leaders are 17, 5 and 2."""
try:
    bar = []
    while True:
        bar.append(int(input()))   # will stop appending if there is any invalid input.
except:
    print("List stopped here")
print('input list is - ', bar)
for1count = 0 # counter for first 'for' loop
for2count = 0 # counter for second 'for' loop
leaders = []
for x in range(0, len(bar)):
    for y in range(x+1, len(bar)):
        if bar[y] >= bar[x]:
            break
        for2count += 1
    if y == len(bar)-1:
        leaders.append(bar[x])
    for1count += 1
print('leaders are - ', leaders)
print('innerloop', for2count, 'outerloop', for1count)
