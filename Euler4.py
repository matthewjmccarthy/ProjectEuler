mylist = [0]
test_num = 0

def pal(s):
    return s == s[::-1]


for i in range(100,1000,1):
    for j in range(100,1000,1):
        s = str((i * j))
        ans = pal(s)
        if ans:
            mylist.append(int(s))
            

mylist.sort()
print(mylist)
