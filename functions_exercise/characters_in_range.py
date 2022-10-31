def chars_in_range(a,b):
    for ch in range(ord(a) + 1, ord(b)):
        result = chr(ch)

        print(result, end=' ')
first = input()
second = input()
chars_in_range(first, second)
