while True:
    new_word = ''
    command = input()
    if command == 'End':
        break
    if command == 'SoftUni':
        continue
    for char in command:
        new_word += char * 2
    print(new_word)