n = int(input())
counter = 0
for _ in range(n):
    current_char = input()
    counter += ord(current_char)

print(f"The sum equals: {counter}")