"""
10-5. Guest Book: Write a while loop that prompts users for their name. Collect
all the names that are entered, and then write these names to a file called
guest_book.txt. Make sure each entry appears on a new line in the file.
"""


from pathlib import Path

path = Path('guest_book.txt')

names = ''
while True:
    print("Enter your name, 'quit' to stop.")
    name = input('--> ')
    if name == 'quit':
        break
    names += name + '\n'

path.write_text(names)
