# Reversed string

name = 'Python'
reversed_string = ''

for char in name :
    reversed_string = char + reversed_string
print(reversed_string)

# Best Approaches using slice

name = "Python"
reversed_string = name[::-1]
print(reversed_string)  # Output: nohtyP

# Best Approaches using the reversed() Function

name = "Python"
reversed_string = ''.join(reversed(name))
print(reversed_string)  # Output: nohtyP
