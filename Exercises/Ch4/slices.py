threes = [num for num in range(3, 31, 3)]

print(f'The first three items in the list are: {threes[0:3]}')
start = ((len(threes)//2)-1)
end = ((len(threes)//2)+2)
print(
    f'Three items from the middle of the list are: {threes[start:end]}')
print(f'The last three items in the list are: {threes[-3:]}')
