n = int(input("Nhập số phần tử: "))
A = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]

# a. Chia hết cho 3 nhưng không chia hết cho 5
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("B:", B)

# b. Bình phương
C = [x**2 for x in A]
print("C:", C)

# c. Ngẫu nhiên từ A chia hết cho 3
import random
D = [x for x in A if x % 3 == 0]
if D:
    print("D:", random.choice(D))
else:
    print("Không có phần tử chia hết cho 3")