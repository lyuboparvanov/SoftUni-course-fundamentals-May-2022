def add_students_to_the_book(student_book, languages_sumbitted):
    while True:
        command = input().split("-")
        if command[0] == 'exam finished':
            break
        name = command[0]
        if command[1] == 'banned':
            del student_book[name]
            continue
        language = command[1]
        points = int(command[2])
        if name not in student_book:
            student_book[name] = {'major': language, 'grade': points}
        else:
            if points > student_book[name]['grade']:
                student_book[name]['grade'] = points
        if language not in languages_sumbitted:
            languages_sumbitted[language] = 1
        else:
            languages_sumbitted[language] += 1
    return student_book


def print_func(student_book, languages_sumbitted):
    print("Results:")
    for el in student_book:
        print(f"{el} | {student_book[el]['grade']}")
    print("Submissions:")
    for k, v in languages_sumbitted.items():
        print(f"{k} - {v}")

def exam_results():
    student_book = {}
    languages_sumbitted = {}
    add_students_to_the_book(student_book, languages_sumbitted)
    print_func(student_book, languages_sumbitted)


                                                                                   
exam_results()