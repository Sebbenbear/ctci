# Replace all spaces in string with %20.
# Assume str has sufficient space at the end to hold extra characters.

def urlify1(string):
    result = [char if char != " " else "%20" for char in string]
    return ''.join(result)

def urlify(string):
    url_params = string.replace(" ", "%20")
    return url_params

result = urlify("the greatest song in the world")
print(result)

result = urlify1("the greatest song in the world")
print(result)