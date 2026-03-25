def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

for i in range(2, 1001):
    if is_prime(i):
        print(i, end=" ")