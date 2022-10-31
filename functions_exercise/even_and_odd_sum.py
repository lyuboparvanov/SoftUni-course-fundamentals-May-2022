def odd_even_sum(nums):
    result = [int(num) for num in nums]
    odd_nums = [num for num in result if num % 2 != 0]
    even_nums = [num for num in result if num % 2 == 0]
    return f"Odd sum = {sum(odd_nums)}, Even sum = {sum(even_nums)}"


numbers = input()
print(odd_even_sum(numbers))