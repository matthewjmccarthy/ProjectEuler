def abNum(n):
    facList = [1]
    for i in range(2, int((n**0.5)+1)):
        if n%i == 0:
            facList.append(i)
            facList.append(n//i)
        i += 1
    facList.sort()
    facList = list(dict.fromkeys(facList))
    if sum(facList) > n:
        return True
    return False

def abCount():
    countList = []
    for n in range(1,28123):
        if abNum(n) == True:
            countList.append(n)
    return countList

def abFunc():
    integers = list(range(0, 28124))
    
    for i in abCount():
        for j in abCount():
            x = i + j
            if integers.count(x) > 0:
                integers.remove(x)
    return integers

print(sum(abFunc()))