import math

def nhap_n():
    """Nhập n là số nguyên dương, nếu n <= 0 thì yêu cầu nhập lại"""
    while True:
        try:
            n = int(input("Nhập n (nguyên dương): "))
            if n > 0:
                return n
            else:
                print("Vui lòng nhập số nguyên dương!")
        except ValueError:
            print("Vui lòng nhập số nguyên!")

# ==================== DÙNG FOR ====================
print("\n=== CÁCH DÙNG VÒNG LẶP FOR ===")
n = nhap_n()

# S1 = 1^2 + 2^2 + ... + n^2
S1_for = 0
for i in range(1, n + 1):
    S1_for += i ** 2
print(f"S1 (for): {S1_for}")

# S2 = 1^3 + 3^3 + ... + (2n+1)^3
S2_for = 0
for i in range(0, n + 1):
    term = 2 * i + 1
    S2_for += term ** 3
print(f"S2 (for): {S2_for}")

# S3 = 2^4 + 4^4 + ... + (2n)^4
S3_for = 0
for i in range(1, n + 1):
    term = 2 * i
    S3_for += term ** 4
print(f"S3 (for): {S3_for}")

# S4 = sum_{i=1}^{n} (-1)^{n-i} * (1/n)
S4_for = 0
for i in range(1, n + 1):
    S4_for += ((-1) ** (n - i)) * (1 / n)
print(f"S4 (for): {S4_for}")

# S5 = 1/2 + 1/(2*3) + 1/(3*4) + ... + 1/(n(n+1))
S5_for = 0
for i in range(1, n + 1):
    S5_for += 1 / (i * (i + 1))
print(f"S5 (for): {S5_for}")

# S6 = 1/sqrt(2) + 1/sqrt(3) + ... + 1/sqrt(n)
S6_for = 0
for i in range(2, n + 1):
    S6_for += 1 / math.sqrt(i)
print(f"S6 (for): {S6_for}")

# ==================== DÙNG WHILE ====================
print("\n=== CÁCH DÙNG VÒNG LẶP WHILE ===")
n = nhap_n()

# S1
S1_while = 0
i = 1
while i <= n:
    S1_while += i ** 2
    i += 1
print(f"S1 (while): {S1_while}")

# S2
S2_while = 0
i = 0
while i <= n:
    term = 2 * i + 1
    S2_while += term ** 3
    i += 1
print(f"S2 (while): {S2_while}")

# S3
S3_while = 0
i = 1
while i <= n:
    term = 2 * i
    S3_while += term ** 4
    i += 1
print(f"S3 (while): {S3_while}")

# S4
S4_while = 0
i = 1
while i <= n:
    S4_while += ((-1) ** (n - i)) * (1 / n)
    i += 1
print(f"S4 (while): {S4_while}")

# S5
S5_while = 0
i = 1
while i <= n:
    S5_while += 1 / (i * (i + 1))
    i += 1
print(f"S5 (while): {S5_while}")

# S6
S6_while = 0
i = 2
while i <= n:
    S6_while += 1 / math.sqrt(i)
    i += 1
print(f"S6 (while): {S6_while}")