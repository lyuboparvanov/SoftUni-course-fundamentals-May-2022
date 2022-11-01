number_of_wagons = int(input())
wagons = [0] * number_of_wagons
while True:

    command = input()

    if command == 'End':
        break

    current_command = command.split()
    type_of_command = current_command[0]
    if type_of_command == 'add':
        value = int(current_command[1])
        wagons[-1] += value
    elif type_of_command == 'insert':
        value = int(current_command[2])
        index = int(current_command[1])
        wagons[index] += value
    elif type_of_command == 'leave':
        index = int(current_command[1])
        value = int(current_command[2])
        wagons[index] -= value
print(wagons)