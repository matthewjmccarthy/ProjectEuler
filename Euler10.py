def primeCheck(num):
    for i in range(2, int(num**.5)+1):
        if num%i == 0:
            return False
    return True

x = 2
plist = []
while x <= 2000000:
    if primeCheck(x):
        plist.append(x)
    x += 1

print(sum(plist))