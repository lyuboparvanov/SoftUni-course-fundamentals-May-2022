def total_sum(product, qty):
    price = 0

    if product == 'coffee':
        price = 1.50
    elif product == 'coke':
        price = 1.40
    elif product == 'water':
        price = 1.00
    elif product == 'snacks':
        price = 2.00
    return f"{price * qty:.2f}"

type_of_product = input()
number_of_orders = int(input())
print(total_sum(type_of_product, number_of_orders))