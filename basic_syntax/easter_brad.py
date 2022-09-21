budget = float(input())
price_flour_kg = float(input())
price_eggs = 0.75 * price_flour_kg
price_for_liter_milk = price_flour_kg + (price_flour_kg * 0.25)
needed_milk_for_loaf = price_for_liter_milk / 4
money_needed_for_one_loaf = needed_milk_for_loaf + price_eggs + price_flour_kg
total_loafs = int(budget / money_needed_for_one_loaf)
colored_eggs = 0
for count in range(1, total_loafs+1):
    colored_eggs += 3
    if count % 3 == 0:
        colored_eggs -= count - 2
diff = abs(budget - (money_needed_for_one_loaf * total_loafs))
print(f"You made {total_loafs} loaves of Easter bread! Now you have {colored_eggs} eggs and {diff:.2f}BGN left.")