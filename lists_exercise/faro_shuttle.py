given_string = input().split()
count_shuffles = int(input())
list = []
for mix in range(count_shuffles):
    list = []
    left_side = given_string[0:len(given_string) // 2]
    righ_side = given_string[len(left_side):]
    for index in range(len(left_side)):
        list.append(left_side[index])
        list.append(righ_side[index])
    given_string = list

print(list)