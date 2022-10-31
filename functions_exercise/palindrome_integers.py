def is_palindrome(nums):
    for current_num in nums:
        if current_num[::-1] == current_num:
            print(True)
        else:
            print(False)

numbers = input().split(', ')
is_palindrome(numbers)