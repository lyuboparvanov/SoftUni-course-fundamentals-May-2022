def registrarion(people):
    for _ in range(people):
        command = input().split()
        type_of_command = command[0]
        person = command[1]
        if type_of_command == 'register':
            reg_id = command[2]
            if person not in register:
                register[person] = reg_id
                print(f"{person} registered {reg_id} successfully")
            else:
                print(f"ERROR: already registered with plate number {reg_id}")
        elif type_of_command == 'unregister':

            if person in register:
                del register[person]
                print(f"{person} unregistered successfully")
            else:
                print(f"ERROR: user {person} not found")

    for k, v in register.items():
        print(f"{k} => {v}")


register = {}
num_of_people = int(input())
registrarion(num_of_people)
