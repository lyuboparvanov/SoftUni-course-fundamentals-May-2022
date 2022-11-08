
def string_repeat(words):
    for word in words:
        result = [word * len(word) for word in words]
        return ''.join(result)


string = input().split()
print(string_repeat(string))