events = input().split("|")
starting_energy = 100
gained_energy = 0
coins = 100
condition = True
for el in events:
    current_event = el.split("-")
    type_of_event = current_event[0]
    number = int(current_event[1])

    if type_of_event == 'rest':
        temp_energy = starting_energy
        starting_energy += number
        if starting_energy > 100:
            starting_energy = 100
        gained_energy = starting_energy - temp_energy

        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {starting_energy}.")

    elif type_of_event == 'order':

        if starting_energy >=30:
            starting_energy -= 30
            coins += number
            print(f"You earned {number} coins.")
        else:
            starting_energy += 50
            if starting_energy > 100:
                starting_energy = 100
            print("You had to rest!")

    else:
        if coins >= number:
            print(f"You bought {type_of_event}.")
            coins -= number
        else:
            print(f"Closed! Cannot afford {type_of_event}.")
            condition = False
            break
if condition:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {starting_energy}")
