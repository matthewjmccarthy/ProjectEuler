sumlist = []
for i in range(1000):
    num = i+1
    sumlist.append(num**num)

total = str(sum(sumlist))
print(total[-10:])