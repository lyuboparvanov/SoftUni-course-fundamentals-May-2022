products = input().split()
to_check = input().split()
dict = {products[key]: int(products[key + 1]) for key in range(0, len(products), 2)}

for current_product in to_check:
    if current_product in dict:
        print(f"We have {dict[current_product]} of {current_product} left")
    else:
        print(f"Sorry, we don't have {current_product}")



