coffee = 0
condition = True
while True:
    command = input()
    if command == 'END':
        break
    if command == 'coding' or command == 'CODING':
        if command.isupper():
            coffee += 1
        coffee += 1
    elif command == 'dog' or command == 'DOG':
        if command.isupper():
            coffee += 1
        coffee += 1
    elif command == 'cat' or command == 'CAT':
        if command.isupper():
            coffee += 1
        coffee += 1
    elif command == 'movie' or command == 'MOVIE':
        if command.isupper():
            coffee += 1
        coffee += 1
    if coffee > 5:
        condition = False
if condition:
    print(coffee)
else:
    print("You need extra sleep")