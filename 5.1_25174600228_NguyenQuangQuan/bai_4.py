while True:
    m = int(input("Nhập m (0 < m): "))
    n = int(input("Nhập n (n > m): "))
    if 0 < m < n:
        break
    print("Lỗi: m và n phải thỏa mãn 0 < m < n. Nhập lại.")

numbers = list(range(m, n + 1, 2))[:100]  # Lấy tối đa 100 số
print("Danh sách:", numbers)
print("Tổng:", sum(numbers))