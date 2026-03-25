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
print("La SNT" if is_prime(n) else "Khong phai SNT")