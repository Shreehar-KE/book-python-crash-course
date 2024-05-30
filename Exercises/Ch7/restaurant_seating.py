"""
7-2. Restaurant Seating: Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message saying 
they'll have to wait for a table. Otherwise, report that their table is ready.
"""


no_of_people = int(input('How many people are in you dinner group?\n--> '))

if no_of_people > 8:
    print('You will have to wait for a table.')
else:
    print('Your table is ready.')
