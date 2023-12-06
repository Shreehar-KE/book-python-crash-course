from random import choice

lottery = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E']

result = []

while len(result) < 4:
    temp = choice(lottery)
    if temp not in result:
        result.append(temp)

print(f'Any ticket matching these {result} wins the prize.')
