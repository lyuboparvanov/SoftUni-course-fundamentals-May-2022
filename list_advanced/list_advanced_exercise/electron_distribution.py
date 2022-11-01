number = int(input())
list = []
counter = 2
factor = 1
while number > 0:
    result = counter * (factor ** 2)
    if result > number:
        list.append(number)
        number -= number
    else:
        list.append(result)
        number -= result
    factor += 1

print(list)



