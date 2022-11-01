def positives(nums):
    result = [num for num in nums if num >= 0]
    return result

def negatives(nums):
    result = [num for num in nums if num < 0]
    return result

def even_nums(nums):
    result = [num for num in nums if num % 2 == 0]
    return result

def odd_nums(nums):
    result = [num for num in nums if num % 2 != 0]
    return result


numbers = list(map(int, input().split(', ')))
print(f"Positive: {', '.join([str(num) for num in positives(numbers)])}")
print(f"Negative: {', '.join([str(num) for num in negatives(numbers)])}")
print(f"Even: {', '.join([str(num) for num in even_nums(numbers)])}")
print(f"Odd: {', '.join([str(num) for num in odd_nums(numbers)])}")
