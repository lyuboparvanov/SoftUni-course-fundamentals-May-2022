gifts = input().split()
index = ''
while True:
    commands = input().split()
    if ' '.join(commands) == "No Money":
        for el in gifts:
            if el != 'None':
                print(el, end=' ')
        break
    current_command = commands[0]
    product = commands[1]
    if len(commands) >= 3:
        index = int(commands[2])

    if current_command == "OutOfStock":
        if product in gifts:
            for el in range(len(gifts)):
                if gifts[el] == product:
                    gifts[el] = 'None'

    elif current_command == "JustInCase":
        gifts.pop()
        gifts.append(product)

    elif current_command == "Required":
        if 0 <= index < len(gifts):
            gifts.pop(index)
            gifts.insert(index, product)

