def ucln(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

m = int(input("Nhap m: "))
n = int(input("Nhap n: "))
print("UCLN =", ucln(m, n))