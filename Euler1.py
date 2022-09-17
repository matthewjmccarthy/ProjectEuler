mylist = []
term = 1

while term < 1000:
    if term%3 == 0:
        mylist.append(term)
        term += 1
    elif term%5 == 0:
        mylist.append(term)
        term += 1
    else:
        term += 1

x = sum(mylist)
print(x)