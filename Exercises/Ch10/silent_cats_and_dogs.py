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
