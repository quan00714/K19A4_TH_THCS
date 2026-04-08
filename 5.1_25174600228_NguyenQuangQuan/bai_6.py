import random

options = ["búa", "kéo", "lá"]
win_rules = {("búa", "kéo"): "thắng", ("kéo", "lá"): "thắng", ("lá", "búa"): "thắng"}

win, lose, draw = 0, 0, 0

for i in range(5):
    player = input(f"Lượt {i+1}: Nhập búa/kéo/lá: ").strip().lower()
    computer = random.choice(options)

    if player not in options:
        print("Nhập sai, tính lượt thua!")
        lose += 1
        continue

    if player == computer:
        draw += 1
        print("Hòa")
    elif (player, computer) in win_rules:
        win += 1
        print("Bạn thắng")
    else:
        lose += 1
        print("Bạn thua")

print(f"Kết quả: Thắng {win}, Hòa {draw}, Thua {lose}")