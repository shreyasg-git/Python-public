foo=list(input("Enter The String : "))
for x in foo:
    if x==' ':
        foo.remove(x)
sng=''
for x in foo:
    sng=sng+str(x)
print(sng)
