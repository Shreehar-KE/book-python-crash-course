"""
10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-7 to fail
silently if either file is missing.
"""


from pathlib import Path

cats_file_path = Path('cats.txt')
dogs_file_path = Path('dogs.txt')

try:
    cats_names = cats_file_path.read_text()
except FileNotFoundError:
    pass
else:
    print('\nThe names of cats are ')
    for name in cats_names.splitlines():
        print(f'  -{name}')

try:
    dogs_names = dogs_file_path.read_text()
except FileNotFoundError:
    pass
else:
    print('\nThe names of cats are ')
    for name in dogs_names.splitlines():
        print(f'  -{name}')
