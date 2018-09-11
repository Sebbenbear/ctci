# Given two strings, write a method to decide if one is a permutation of the other.
# Time Complexity: O(max(n log n, m log m))
# Space Complexity: O(n + m)
def checkPermutation(first_str, second_str):
    return sorted(first_str) == sorted(second_str)

result = checkPermutation("algorithm", "logarithm")
print(result)

result = checkPermutation("algor", "logarithm")
print(result)

result = checkPermutation("algorithm", "logarithms")
print(result)