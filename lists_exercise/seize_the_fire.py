command = input().split("#")
water = int(input())

cells = []
total_fires = 0
effort = 0

for el in command:
    current_command = el.split(" = ")
    type_of_fire = current_command[0]
    capacity = int(current_command[1])
    condition = False
    if water < capacity:
        continue
    if type_of_fire == "High":
        if 81 <= capacity <= 125:
            condition = True

    elif type_of_fire == 'Medium':
        if 51 <= capacity <= 80:
            condition = True

    elif type_of_fire == 'Low':
        if 1 <= capacity <= 50:
           condition = True

    if condition:
        water -= capacity
        cells.append(capacity)
        total_fires += capacity
        effort = total_fires * 0.25
print(f"Cells:")
for cell in cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")

print(f"Total Fire: {total_fires}")


