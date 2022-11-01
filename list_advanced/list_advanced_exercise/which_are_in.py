example_first = input().split(', ')
example_second = input().split(', ')
final_lst = []

for word in example_first:
    for word_two in example_second:
        if word in word_two:
            final_lst.append(word)
            break

print(final_lst)