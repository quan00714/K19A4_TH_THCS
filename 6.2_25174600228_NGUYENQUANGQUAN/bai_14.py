n = int(input("Nhập số lượng tuple: "))
tuples = []
for _ in range(n):
    name = input("Nhập name: ")
    age = int(input("Nhập age: "))
    score = int(input("Nhập score: "))
    tuples.append((name, age, score))
tuples.sort(key=lambda x: (x[0], x[1], x[2]))
print("Sau khi sắp xếp:", tuples)