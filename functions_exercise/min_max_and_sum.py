def min_max_and_sum_func(nums):
    smallest_num = min(nums)
    biggest_num = max(nums)
    sum_of_nums = sum(nums)

    return f"The minimum number is {smallest_num}\n" \
           f"The maximum number is {biggest_num}\n" \
           f"The sum number is: {sum_of_nums}"

numbers = list(map(int, input().split()))
print(min_max_and_sum_func(numbers))