lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
helmets = 0
swords = 0
shields = 0
armors = 0
for battle in range(1, lost_fights + 1):
    if battle % 2 == 0:
        helmets += 1
    if battle % 3 == 0:
        swords += 1
    if battle % 6 == 0:
        shields += 1
    if battle % 12 == 0:
        armors += 1

total = (helmet_price * helmets) + (armor_price * armors) + (shield_price * shields) + (sword_price * swords)
print(f"Gladiator expenses: {total:.2f} aureus")