"""
10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file. Write
a program that tries to read these files and print the contents of the file to the
screen. Wrap your code in a try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing. Move one of the files to a dif-
ferent location on your system, and make sure the code in the except block
executes properly.
"""


from pathlib import Path

cats_file_path = Path('cats.txt')
dogs_file_path = Path('dogs.txt')

try:
    cats_names = cats_file_path.read_text()
except FileNotFoundError:
    print('\ncats.txt is not found at given path...!')
else:
    print('\nThe names of cats are ')
    for name in cats_names.splitlines():
        print(f'  -{name}')

try:
    dogs_names = dogs_file_path.read_text()
except FileNotFoundError:
    print('\ndogs.txt is not found at given path...!')
else:
    print('\nThe names of cats are ')
    for name in dogs_names.splitlines():
        print(f'  -{name}')
