dict = {}

example = ''.join(input().split())

for ch in example:
    if ch not in dict:
        dict[ch] = 0
    dict[ch] += 1

for k, v in dict.items():
    print(f"{k} -> {v}")