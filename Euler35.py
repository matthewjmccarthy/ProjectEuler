def split(n):
    n = str(n)
    digits = []
    for i in n:
        digits.append(int(i))
    return digits

def combine(n):
    a = 0
    for i in range(0,len(n)):
        a += n[i] * (10**(len(n)-i-1))
    return a

def isPrime(n):
    for i in range(2, int(n**0.5) +1):
        if n%i == 0:
            return False
    return True

def rotate(n):
    x = split(n)
    cycList = []
    for i in range(0,len(x)):
        newnum = []
        for j in x:
            a = x.index(j)
            newnum.append(x[(a+i)%len(x)])
        cycList.append(combine(newnum))
    return cycList

def checkRot(n):
    for i in rotate(n):
        if isPrime(i) == False:
            return False
    return True

cycPrimes = []
for i in range(2,1000001):
    if checkRot(i) == True:
        cycPrimes.append(i)

print(str(len(cycPrimes))+' : '+str(cycPrimes))
