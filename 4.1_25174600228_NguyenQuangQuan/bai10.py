# Nguyen to
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

n = int(input("Nhap n: "))
for i in range(2, n+1):
    if is_prime(i):
        print(i, end=" ")
        
        
# So hoan Hao
def is_perfect(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s == n

n = int(input("Nhap n: "))
for i in range(1, n+1):
    if is_perfect(i):
        print(i, end=" ")        