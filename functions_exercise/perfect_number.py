def perfect_num_func(num):
    sum_of_nums = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_nums += i
    if sum_of_nums == num:
        return "We have a perfect number!"
    return "It's not so perfect."

number = int(input())
print(perfect_num_func(number))