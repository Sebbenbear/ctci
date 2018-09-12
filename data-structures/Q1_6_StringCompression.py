# Perform basic string compression using counts of repeated characters
# aabcccccaaa => a2b1c5a3
# if compressed string isn't smaller, return original string
# assume upper case and lower case letters

# O(n) time, O(1) space
def compress(word):
    if len(word) < 2:
        return word
    result = ''
    idx = 0
    prev_char = word[0]
    count = 1
    while idx < len(word):
        next_char = word[idx]
        if prev_char != next_char and prev_char != '':
            result = result + prev_char
            result = result + str(count)
            prev_char = next_char
            count = 1
        else:
            count += 1
        idx += 1
    result = result + prev_char
    result = result + str(count)

    # return result
    if len(result) < len(word):
        return result
    else:
        return word

result = compress("aabcccccaaa")
print(result)

result = compress("ab")
print(result)

result = compress("")
print(result)

result = compress("aaaabbbbb")
print(result)