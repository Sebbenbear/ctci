# Check if a word is a permutation of a palindrome.
# Palindrome: arrangement of letters
# Permutation: rearrangement of letters
from collections import Counter
import string

# 1. Convert to lower case, ignore or remove spaces/punctuation
# 2. If it has all pairs, or only one letter by itself, it's a permutation of a palindrome
# Runtime: O(n). n for adding to Counter, n for checking values.
# Space: O(n) for creating dictionary, n for the normalised string
def palindromePermutation(word):
    normalised_word = word.lower().translate(str.maketrans('', '', string.whitespace))
    c = Counter(normalised_word)

    single_not_found = True
    for frequency in c.values():
        if frequency % 2 == 0: # there's an even number, so can make a palindrome
            continue
        elif frequency == 1 and single_not_found:
            single_not_found = False # we've found the single frequency
            continue
        else:
            return False
    return True

result = palindromePermutation("Tact Coa")
print(result)

result = palindromePermutation("Tact oa")
print(result)

result = palindromePermutation("T")
print(result)

result = palindromePermutation("")
print(result)