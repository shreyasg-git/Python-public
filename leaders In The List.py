
try:
    bar=[]
    while True:
            bar.append(int(input()))
except:
    print("List stopped here")

for x in range(0,len(bar)):
    for y in range(x+1,len(bar)):
        if bar[y]>=bar[x]:
            break
    if y==len(bar)-1:
        print(bar[x])
