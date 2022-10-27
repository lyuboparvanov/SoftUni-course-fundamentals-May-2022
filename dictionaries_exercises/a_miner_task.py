dict = {}

while True:
    command = input()
    if command == 'stop':
        break

    value = int(input())

    if command not in dict:
        dict[command] = 0
    dict[command] += value

for k, v in dict.items():
    print(f"{k} -> {v}")
