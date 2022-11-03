numbers = input().split(" ")
nums_to_remove = int(input())
list = [int(numbers) for numbers in numbers]
for times in range(nums_to_remove):
    list.remove(min(list))

list = [str(num) for num in list]

print(', '.join(list))