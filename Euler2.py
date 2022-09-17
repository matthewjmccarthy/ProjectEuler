fiblist = [0,1]
while fiblist[-1] < 4000000:
    fiblist.append(fiblist[-1] + fiblist[-2])


newlist = []
for x in fiblist:
    if x%2 == 0:
        newlist.append(x)
        

print(sum(newlist))