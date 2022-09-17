from math import prod

def fac(n):
    facList = []
    x = 1
    while x <= n:
        facList.append(x)
        x += 1
    return prod(facList)

num = str(fac(100))
numList = []

for i in num:
    numList.append(int(i))
print(sum(numList))