textfile = open('p054_poker.txt','r')
line = textfile.readlines()

def check(hand):
    




i = 0
p1 = []
p2 = []
line[i] = line[i].rstrip('\n')
l = line[i].split(' ')
p1 = l[0:5]
p2 = l[5:10]

check(p1)
check(p2)
print(p1, p2)

textfile.close()