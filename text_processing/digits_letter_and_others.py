def ch_extractions_digits(word):
    return ''.join([str(ch) for ch in word if ch.isdigit()])

def ch_extractions_letters(word):
    return ''.join([ch for ch in word if ch.isalpha()])
def ch_extractions_symbols(word):
    return ''.join([ch for ch in word if not ch.isalpha() and  not ch.isdigit()])


example = input()
print(ch_extractions_digits(example))
print(ch_extractions_letters(example))
print(ch_extractions_symbols(example))