"""
9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters.
Randomly select 4 numbers or letters from the list and print a message saying that
any ticket matching these 4 numbers or letters wins a prize.
"""


from random import choice

lottery = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E']

result = []

while len(result) < 4:
    temp = choice(lottery)
    if temp not in result:
        result.append(temp)

print(f'Any ticket matching these {result} wins the prize.')
