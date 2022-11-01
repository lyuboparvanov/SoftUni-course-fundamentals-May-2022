
given_words = input().split()
the_palindrome = input()
found_palindromes = []

for word in given_words:
    if word[::-1] == word:
        found_palindromes.append(word)

print(found_palindromes)
print(f"Found palindrome {found_palindromes.count(the_palindrome)} times")