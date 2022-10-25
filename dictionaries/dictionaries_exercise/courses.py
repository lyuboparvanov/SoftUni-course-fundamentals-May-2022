courses = {}


while True:
    command = input()
    if command == 'end':
        break

    name_of_class, student = command.split(" : ")
    if name_of_class not in courses:
        courses[name_of_class] = [student]
    else:
        courses[name_of_class].append(student)

for key, value in courses.items():
    print(f"{key}: {len(value)}")
    for student in courses[key]:
        print(f"-- {''.join(student)}")
