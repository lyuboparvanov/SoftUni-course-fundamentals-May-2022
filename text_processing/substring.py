def substring(word, word2):
    while word in word2:
        word2 = word2.replace(word, '')
    return word2


print(substring(input(), input()))
