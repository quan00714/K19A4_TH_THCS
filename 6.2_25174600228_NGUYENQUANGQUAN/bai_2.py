n = int(input("Nhập số phần tử: "))
a = []
for i in range(n):
    a.append(int(input(f"Nhập phần tử thứ {i+1}: ")))

# a. Phần tử lớn thứ hai và vị trí
b = sorted(set(a), reverse=True)
if len(b) >= 2:
    max2 = b[1]
    print("Phần tử lớn thứ hai:", max2)
    print("Vị trí:", [i for i, x in enumerate(a) if x == max2])
else:
    print("Không có phần tử lớn thứ hai")

# b. Số lượng số dương liên tiếp nhiều nhất
max_len = 0
cur_len = 0
for x in a:
    if x > 0:
        cur_len += 1
        max_len = max(max_len, cur_len)
    else:
        cur_len = 0
print("Số lượng số dương liên tiếp nhiều nhất:", max_len)

# c. Số lượng số dương liên tiếp có tổng lớn nhất
max_sum = 0
cur_sum = 0
best_count = 0
cur_count = 0
for x in a:
    if x > 0:
        cur_sum += x
        cur_count += 1
        if cur_sum > max_sum:
            max_sum = cur_sum
            best_count = cur_count
    else:
        cur_sum = 0
        cur_count = 0
print("Số lượng số dương liên tiếp có tổng lớn nhất:", best_count)