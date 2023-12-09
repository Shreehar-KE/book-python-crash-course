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
