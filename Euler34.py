def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

def split(n):
    n = str(n)
    digits = []
    for i in n:
        digits.append(int(i))
    return digits

sumlist = []
for i in range(3,1000000):
    x = split(i)
    newnum = []
    for j in x:
        newnum.append(fact(j))
    if sum(newnum) == i:
        sumlist.append(i)
        print(i)
print(sum(sumlist), sumlist)