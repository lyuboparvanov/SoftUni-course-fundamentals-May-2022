given_string = input().split(", ")
beggars = int(input())
numbers = [int(given_string) for given_string in given_string]
list = []

for current_beggar in range(beggars):
    sum_taken = 0

    for index in range(current_beggar, len(numbers), beggars):
        sum_taken += numbers[index]
    list.append(sum_taken)

print(list)