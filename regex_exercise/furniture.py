import re
items = []
total = 0
while True:
    data = input()
    if data == 'Purchase':
        break

    pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"

    matches = re.match(pattern, data)
    if matches:
        price = matches.group(2)
        qty = matches.group(3)
        total += float(price) * int(qty)
        item = matches.group(1)
        items.append(item)


print(f"Bought furniture:")
if len(items) > 0:
    print('\n'.join(items))
print(f"Total money spend: {total:.2f}")

