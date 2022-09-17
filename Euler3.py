import math
sqrt = math.sqrt

x = 600851475143
for i in range(3,int(sqrt(x))+1,2): 
    if x%i == 0:
        print(i)
        x = x/i