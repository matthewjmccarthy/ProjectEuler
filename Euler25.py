def fib(n):
    fibList = [1, 1]
    while len(str(fibList[-1])) < n:
        fibList.append(fibList[-1] + fibList[-2])
    print(len(fibList))

fib(1000)