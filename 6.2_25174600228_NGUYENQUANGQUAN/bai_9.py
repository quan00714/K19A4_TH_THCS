n = int(input("Nhập số phần tử: "))
a = []
for i in range(n):
    a.append(int(input(f"Nhập phần tử thứ {i+1}: ")))

for x in a:
    assert x % 2 == 0, "Danh sách chứa số lẻ"
print("Tất cả đều là số chẵn")