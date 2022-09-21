first_word = input()
second_word = input()
new_word = first_word
for char in range(len(second_word)):
    left_side = second_word[:char + 1]
    righ_side = first_word[char + 1:]
    current_word = left_side + righ_side
    if current_word == new_word:
        continue
    print(current_word)
    new_word = current_word
