import random
A = [random.randint(1, 99999) for _ in range(1000)]

# Cách 1: dùng sorted()
sorted_A1 = sorted(A)

# Cách 2: không dùng sorted() (bubble sort)
sorted_A2 = A[:]
n = len(sorted_A2)
for i in range(n):
    for j in range(0, n-i-1):
        if sorted_A2[j] > sorted_A2[j+1]:
            sorted_A2[j], sorted_A2[j+1] = sorted_A2[j+1], sorted_A2[j]

print("Đã sắp xếp bằng 2 cách")