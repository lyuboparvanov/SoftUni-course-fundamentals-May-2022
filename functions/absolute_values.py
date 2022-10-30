def absolute_value_func(nums):
    result = [abs(float) for float in nums]
    return result
numbers = list(map(float, input().split()))
print(absolute_value_func(numbers))

