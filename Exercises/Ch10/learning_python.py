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
