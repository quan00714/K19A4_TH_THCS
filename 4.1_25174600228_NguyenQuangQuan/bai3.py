def nhan_an_do(a, b):
    res = 0
    while b > 0:
        if b % 2 == 1:
            res += a
        a *= 2
        b //= 2
    return res

x = int(input("Nhap a: "))
y = int(input("Nhap b: "))
print("Ket qua =", nhan_an_do(x, y))