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
