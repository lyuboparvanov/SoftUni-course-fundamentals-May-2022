def calculations_func(current_operation, a, b):
    result = 0
    if current_operation == 'multiply':
        result = a * b
    elif current_operation == 'divide':
        result = a / b
    elif current_operation == 'subtract':
        result = a - b
    elif current_operation == 'add':
        result = a + b
    return int(result)


type_of_operation = input()
first_num = int(input())
second_num = int(input())
print(calculations_func(type_of_operation, first_num, second_num))