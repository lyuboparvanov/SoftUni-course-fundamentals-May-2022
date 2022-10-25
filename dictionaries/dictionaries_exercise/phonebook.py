phonebook = {}

while True:
    command = input()
    if "-" not in command:
        break

    person, number = command.split("-")
    if person not in phonebook:
        phonebook[person] = number
    phonebook[person] = number

for names_to_check in range(int(command)):
    current_name = input()
    if current_name not in phonebook:
        print(f"Contact {current_name} does not exist.")
    else:
        print(f"{current_name} -> {phonebook[current_name]}")
