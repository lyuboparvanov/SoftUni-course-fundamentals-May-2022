nums = list(map(int, input().split()))
factor = int(input())
scores = [num * factor for num in nums]

bigger_nums = [num for num in scores if num >= sum(nums)/ len(nums)]
print(bigger_nums)