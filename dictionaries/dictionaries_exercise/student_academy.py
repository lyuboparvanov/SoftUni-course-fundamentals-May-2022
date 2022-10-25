def grades(students):
    for _ in range(students):
        name = input()
        grade = float(input())

        if name not in grades_book:
            grades_book[name] = [grade]
        else:
            grades_book[name] += [grade]

    for k, v in grades_book.items():
        if sum(v) / len(v) >= 4.50:
            print(f"{k} -> {sum(v) / len(v):.2f}")


grades_book = {}
number_of_students = int(input())
grades(number_of_students)