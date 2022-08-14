a = str(input("enter the String"))
print(a)
len(a)
c = (len(a))
print(c)
if c > 7:
    i = 1
    while i < c:
        print(a[i])
        i = i +2
else:
    i = 0
    while i < c:
        print(a[i])
        i = i +2
