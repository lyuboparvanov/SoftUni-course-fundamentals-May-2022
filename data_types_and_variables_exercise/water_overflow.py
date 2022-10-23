n = int(input())
tank = 0
for _ in range(n):
    current_liters = int(input())
    tank +=  current_liters
    if tank > 255:
        print(f"Insufficient capacity!")
        tank -= current_liters

print(tank)