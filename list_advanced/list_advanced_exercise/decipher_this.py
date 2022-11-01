message = input().split()
result = []
for current_word in message:
    symbol = ''
    word = ''
    for ch in current_word:
        if ch.isdigit():
            symbol += ch
        else:
            word += ch
    if len(word) >= 2:
        new_word = chr(int(symbol)) + (word[-1:] + word[1:-1] + word[:1])
    else:
        new_word = chr(int(symbol)) + word
    result.append(new_word)

print(' '.join(result))