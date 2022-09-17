def collatz(n):
    collList = []
    while n > 1:
        collList.append(int(n))
        if n%2 == 0:
            n = n/2
        else:
            n = (3*n) + 1
    collList.append(1)
    return len(collList)

x = 1
mylist = []
while x <= 1000000:
    mylist.append(collatz(x))
    x += 1

print(mylist)
print(mylist.index(max(mylist)) + 1)