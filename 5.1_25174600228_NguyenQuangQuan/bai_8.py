nums = []
while True:
    val = int(input("Nhập số nguyên (0 để dừng): "))
    if val == 0:
        break
    nums.append(val)

print("Danh sách:", nums)

# 8a: Tìm x
x = int(input("Nhập x cần tìm: "))
indices = [i for i, v in enumerate(nums) if v == x]
if indices:
    print("Vị trí tìm thấy x:", indices)
else:
    print("Không tìm thấy x")

# 8b: Sửa giá trị x
if indices:
    pos = indices[0]
    new_val = int(input(f"Nhập giá trị mới cho vị trí {pos}: "))
    nums[pos] = new_val
    print("Sau sửa:", nums)

# 8c: Thêm y
y = int(input("Nhập y để thêm: "))
pos_type = input("Thêm vào (đầu/cuối/giữa): ").strip().lower()
if pos_type == "đầu":
    nums.insert(0, y)
elif pos_type == "cuối":
    nums.append(y)
else:  # giữa
    mid = len(nums) // 2
    nums.insert(mid, y)
print("Sau thêm:", nums)

# 8d: Sắp xếp giảm dần (không dùng sort)
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] < nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
print("Sau sắp xếp giảm dần:", nums)

# 8e: Xóa phần tử
del_pos = int(input("Nhập vị trí cần xóa: "))
if 0 <= del_pos < len(nums):
    del nums[del_pos]
print("Sau xóa:", nums)