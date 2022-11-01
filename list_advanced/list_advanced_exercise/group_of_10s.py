numbers = sorted(list(map(int, input().split(", "))))
current_list = []
group = 0


while len(numbers) > 0:
    for current_num in range(len(numbers)):
        if 0 <= numbers[current_num] < 10:
            current_list.append(current_num)
            numbers.remove(current_num)
            print(current_list)
        # elif 10 <= current_num < 20:
        #     pass
        # elif 20 <= current_num < 30:
        #     pass
        # elif 30 <= current_num < 40:
        #     pass
        # elif current_num >= 50:
        #     pass

