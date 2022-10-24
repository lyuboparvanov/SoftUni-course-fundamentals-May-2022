n = int(input())
open_brackets = 0
closing_brackets = 0

for _ in range(n):
    current_symbol = input()
    if current_symbol == ')':
        closing_brackets += 1
    elif current_symbol == '(':
        open_brackets += 1
if open_brackets == closing_brackets:
    print("BALANCED")
else:
    print("UNBALANCED")
