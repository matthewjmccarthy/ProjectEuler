def prime_check(num):
    for i in range(2, int(num**.5)+1):
        if num%i == 0:
            return False
    return True

print(prime_check(3))