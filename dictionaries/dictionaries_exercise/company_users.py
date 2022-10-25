employees = {}

while True:
    command = input()
    if command == 'End':
        break
    company, id = command.split(f" -> ")

    if company not in employees:
        employees[company] = [id]
    if id not in employees[company]:
            employees[company].append(id)


for k in employees.keys():
    print(k)
    for value in employees[k]:
        print(f"-- {''.join(value)}")