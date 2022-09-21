num_commands = int(input())

for commands in range(num_commands):
    current_command = int(input())
    if current_command == 88:
        print("Hello")
    elif current_command == 86:
        print("How are you?")

    elif current_command != 88 and current_command != 86 and current_command < 88:
        print("GREAT!")

    elif current_command > 88:
        print("Bye.")