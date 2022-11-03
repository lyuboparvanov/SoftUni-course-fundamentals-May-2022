products = input().split("|")
budget = float(input())
bought_products = []
final_profit = 0
sum_profit = 0
sum_final_profit = 0
for product in products:
    current_product = product.split("->")
    type_of_product = current_product[0]
    price = float(current_product[1])
    condition = False
    if budget < price:
        continue
    if type_of_product == "Clothes":
        if price <= 50.00:
            condition = True

    elif type_of_product == "Shoes":
        if price <= 35.00:
            condition = True
    elif type_of_product == "Accessories":
        if price <= 20.50:
            condition = True

    if condition:
        budget -= price
        bought_products.append(price)

for items in bought_products:
    profit = items * 0.40
    sum_profit += profit
    final_profit = items + items * 0.40
    sum_final_profit += final_profit
    print(f"{final_profit:.2f}" ,end=' '"")
print()
print(f"Profit: {sum_profit:.2f}")

if budget + sum_final_profit  >= 150:
    print(f"Hello, France!")
else:
    print(f"Not enough money.")