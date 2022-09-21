divisor = int(input())
boundary = int(input())
highest_num = ''
for num in range(divisor, boundary + 1):
    if num % divisor == 0:
        highest_num = num
print(highest_num)