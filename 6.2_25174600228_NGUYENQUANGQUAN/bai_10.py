import random
lst = [x for x in range(0, 201) if x % 5 == 0 and x % 7 == 0]
print("Số ngẫu nhiên:", random.choice(lst))