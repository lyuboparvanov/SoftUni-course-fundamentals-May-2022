number_of_orders = int(input())
grand_total = 0
for _ in range(number_of_orders):
    price_per_capsule = float(input())
    num_of_days = int(input())
    needed_capsules_per_day = int(input())
    if 0.01 > price_per_capsule or number_of_orders > 100.00:
        continue
    elif 1 > num_of_days or num_of_days > 31:
        continue
    elif 1 > needed_capsules_per_day or needed_capsules_per_day > 2000:
        continue
    total = (price_per_capsule * needed_capsules_per_day) * num_of_days
    grand_total += total
    print(f"The price for the coffee is: ${total:.2f}")
print(f"Total: ${grand_total:.2f}")
