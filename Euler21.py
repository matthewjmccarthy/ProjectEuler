def d(n):
    divList = [1]
    for i in range(2, int((n**0.5)+1)):
        if n%i == 0:
            divList.append(i)
            divList.append(n//i)
    divList = list(dict.fromkeys(divList))
    divList.sort()
    return sum(divList)

amList = []
for i in range(3, 10001):
    if d(d(i)) == i and d(i) != i:
        amList.append(i)

print(amList)
