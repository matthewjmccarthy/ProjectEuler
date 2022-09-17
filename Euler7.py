def primeCheck(num):
    for i in range(2, int(num**.5)+1):
        if num%i == 0:
            return False
    return True

plist = []
x = 1
while len(plist) <= 10001:
    if primeCheck(x):
        plist.append(x)
    x += 1

print(plist[-1])