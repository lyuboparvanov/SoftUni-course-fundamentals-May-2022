def grades_func(score):
    result = None
    if 2.00 <= score <= 2.99:
        result = 'Fail'
    elif 3.00 <= score <= 3.49:
        result = 'Poor'
    elif 3.50 <= score <= 4.49:
        result = 'Good'
    elif 4.50 <= score <= 5.49:
        result = 'Very Good'
    elif score > 5.49:
        result = 'Excellent'
    return result


current_grade = float(input())
print(grades_func(current_grade))