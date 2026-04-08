n = int(input("Nhập số lượng phần tử của tuple: "))
numbers = tuple(int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n))

odd_tuple = tuple(x for x in numbers if x % 2 == 1)
print("Tuple chứa số lẻ:", odd_tuple)