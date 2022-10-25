dict = {}

while True:
    command = input()
    if command == 'statistics':
        break

    key, value = command.split(': ')

    if key not in dict:
        dict[key] = int(value)
    else:
        dict[key] += int(value)


result = [f"- {key}: {str(dict[key])}" for key in dict]
print("Products in stock:")
print(f"\n"''.join(result))
print(f"Total Products: {len(dict.keys())}")
print(f"Total Quantity: {sum(dict.values())}")
