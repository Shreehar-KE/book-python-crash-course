"""
2-7. Stripping Names: Use a variable to represent a person's name, and
include some whitespace characters at the beginning and end of the name.
Make sure you use each character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(),
rstrip(), and strip().
"""

name_1 = "\tShreeharK E "
name_2 = " \nIvy "

print(name_1+"__")
print(name_1.rstrip()+"__")
print(name_1.lstrip()+"__")
print(name_1.strip()+"__")
print()
print(name_2+"__")
print(name_2.rstrip()+"__")
print(name_2.lstrip()+"__")
print(name_2.strip()+"__")
