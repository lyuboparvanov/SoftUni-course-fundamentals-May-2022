from math import floor

group_size = int(input())
num_of_days = int(input())
companions = group_size
coins = 0
for day in range(1, num_of_days + 1):
    if day % 10 == 0:
        companions -= 2
    if day % 15 == 0:
        companions += 5

    if day % 3 == 0:
        coins -= 3 * companions
    if day % 5 == 0:
        coins += 20 * companions
        if day % 3 == 0:
            coins -= 2 * companions
    coins += 50 - (2 * companions)

total = coins // companions

print(f"{companions} companions received {total} coins each.")
