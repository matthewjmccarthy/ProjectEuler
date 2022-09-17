smallList = []
bigList = []

for n in range(1,101):
    smallList.append(n**2)

for x in range(1,101):
    bigList.append(x)

smallSum = sum(smallList)
bigSum = (sum(bigList))**2
total = bigSum - smallSum

print(total)