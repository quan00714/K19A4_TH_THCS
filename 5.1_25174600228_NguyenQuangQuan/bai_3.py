while True:
    m = int(input("Nhập m (0 < m): "))
    n = int(input("Nhập n (n > m): "))
    if 0 < m < n:
        break
    print("Lỗi: m và n phải thỏa mãn 0 < m < n. Nhập lại.")

numbers = list(range(m, n + 1))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Danh sách số chẵn:", even_numbers)