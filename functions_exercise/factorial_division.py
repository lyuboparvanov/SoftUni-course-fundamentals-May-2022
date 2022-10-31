def factorial_sum(a, b):
    for i in range(1, a):
        a *= i
    for y in range(1, b):
        b *= y
    return f"{a / b:.2f}"


first_num = int(input())
second_num = int(input())
print(factorial_sum(first_num, second_num))