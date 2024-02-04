threes = [num for num in range(3, 31, 3)]

print('The first three items in the list are:')
for num in threes[:3]:
    print(num)

print('\nThree items from the middle of the list are:')
middle = len(threes)//2 - 1
for num in threes[middle: middle+3]:
    print(num)

print('\nThe last three items in the list are:')
for num in threes[-3:]:
    print(num)
