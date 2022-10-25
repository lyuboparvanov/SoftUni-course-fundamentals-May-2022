products = {}
pricings = {}

while True:

    command = input()
    if command == 'buy':
        break

    current_command = command.split()
    name = current_command[0]
    price = float(current_command[1])
    qty = int(current_command[2])

    if name not in products:
        products[name] = qty
        pricings[name] = price
    else:
        products[name] += qty
        pricings[name] = price

name_of_product = [key for key in products.keys()]
amount_of_items = [value for value in products.values()]
prices = [value for value in pricings.values()]
total = [f"{name_of_product[key]} -> {prices[key] * amount_of_items[key]:.2f}" for key in range(len(amount_of_items))]
print('\n'.join(total))