# Three types of edits on strings:
# - insert char
# - remove char
# - replace char
# Given two strings, return true if they are one edit distance or less away.

# O(n) time, O(1) additional space
def editDistance(first, second):
    ptrA, ptrB = 0, 0
    edit_distance = 0
    while ptrA < len(first)-1 and ptrB < len(second)-1:
        if first[ptrA] == second[ptrB]:
            # they are the same
            ptrA += 1
            ptrB += 1
        elif first[ptrA] == second[ptrB+1]:
            # insertion in B, or deletion in A
            ptrB += 1
        elif first[ptrA+1] == second[ptrB]:
            # insertion in A, or deletion in B
            ptrA += 1
        else:
            # they are both different and it's a substitution
            ptrA += 1
            ptrB += 1
            edit_distance += 1

    edit_distance += abs(len(first) - len(second))

    return edit_distance < 2

result = editDistance("pale", "ple") # true
print(result)

result = editDistance("pales", "pale") # true
print(result)

result = editDistance("pale", "bale") # true
print(result)

result = editDistance("pale", "bake") # false
print(result)

result = editDistance("pale", "") # false
print(result)

result = editDistance("pale", "a") # false
print(result)
