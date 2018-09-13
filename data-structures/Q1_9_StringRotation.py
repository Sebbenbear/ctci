
# String Rotation: Assume you have amethod isSubstring which checks if one word is a 
# substring of another. Given two strings, 51 and 52, write code to check if 52 is a 
# rotation of 51 using only one call to isSubstring (e.g.,"waterbottle"is a rotation of"erbottlewat").

#O(1) space
def stringRotation(s1, s2):
    for i in range(len(s1)):      # O(n)
        if s1 == s2[i:] + s2[:i]: # O(n)
            return True
    return False

result = stringRotation("waterbottle", "erbottlewat")
print(result)