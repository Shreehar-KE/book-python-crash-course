"""
4-10. Slices: Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to
  print the first three items from that program’s list.

• Print the message Three items from the middle of the list are:. Then use a
  slice to print three items from the middle of the list.

• Print the message The last three items in the list are:. Then use a slice to
  print the last three items in the list.
"""


threes = [num for num in range(3, 31, 3)]

print('The first three items in the list are:')
for num in threes[:3]:
    print(num)

print('\nThree items from the middle of the list are:')
middle = len(threes)//2
for num in threes[middle-1: middle+2]:
    print(num)

print('\nThe last three items in the list are:')
for num in threes[-3:]:
    print(num)
