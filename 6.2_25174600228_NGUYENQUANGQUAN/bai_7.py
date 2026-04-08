List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]

# a. In danh sách
print("Danh sách:", List_)

# b. Phần tử thứ hai, vị trí thứ 3 của sublist
print("Phần tử thứ hai, vị trí thứ 3:", List_[2][1])

# c. Độ dài và thêm sublist ngẫu nhiên
print("Độ dài:", len(List_))
List_.append(["extra", 999])
print("Sau khi thêm:", List_)

# d. Tổng sale thứ hai, thứ ba, thứ bảy, chủ nhật
tong = List_[1][1] + List_[2][1] + List_[5][1] + List_[6][1]
print("Tổng sale các ngày:", tong)