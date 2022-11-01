
employee_scores = list(map(int, input().split()))
factor = int(input())

employee = list(map(lambda x: x * factor, employee_scores))
average_score = sum(employee_scores) // len(employee_scores)
grades_higher_than_average = [num for num in employee_scores if num > average_score]

if len(grades_higher_than_average) > average_score:
    print(f"Score: {len(grades_higher_than_average)}/{len(employee_scores)}. Employees are happy!")
else:
    print(f"Score: {len(grades_higher_than_average)}/{len(employee_scores)}. Employees are not happy!")