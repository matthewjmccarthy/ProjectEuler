import math
prod = math.prod

for a in range(1, 1000):
    for b in range(1, 1000):
        for c in range(1, 1000):
            if ((a**2 + b**2)**0.5) == c and a + b + c == 1000:
                print(a, b, c)
                print(prod([a, b, c]))