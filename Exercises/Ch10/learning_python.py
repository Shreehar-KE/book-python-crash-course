"""
10-1. Learning Python: Open a blank file in your text editor and write a few lines
summarizing what you’ve learned about Python so far. Start each line with the
phrase In Python you can. . . . Save the file as learning_python.txt in the same
directory as your exercises from this chapter. Write a program that reads the file
and prints what you wrote two times: print the contents once by reading in the
entire file, and once by storing the lines in a list and then looping over each line.
"""

"""
10-3. Simpler Code: The program file_reader.py in this section uses a temporary
variable, lines, to show how splitlines() works. You can skip the temporary
variable and loop directly over the list that splitlines() returns:

for line in contents.splitlines():

      Remove the temporary variable from each of the programs in this section,
to make them more concise.
"""


from pathlib import Path
path = Path('learning_python.txt')
contents = path.read_text().rstrip()
print('\nPrinting as a whole\n')
print(contents)

print('\nPrinting line by line\n')
# lines = contents.splitlines()
# for line in lines:
for line in contents.splitlines():  # 10-3.simpler_code
    print(line)
