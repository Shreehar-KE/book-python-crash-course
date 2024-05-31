"""
10-2. Learning C: You can use the replace() method to replace any word in a
string with a different word. Here's a quick example showing how to replace
'dog' with 'cat' in a sentence:

>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
'I really like cats.'

      Read in each line from the file you just created, learning_python.txt, 
and replace the word Python with the name of another language, such as C. Print
each modified line to the screen.
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

# To replace as a whole
# print(contents.replace('python', 'c'))

# To replace line by line
# lines = contents.splitlines()
# for line in lines:
for line in contents.splitlines():  # 10-3.simpler_code
    print(line.replace('python', 'c'))
