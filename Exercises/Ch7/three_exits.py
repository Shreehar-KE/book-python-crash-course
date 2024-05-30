"""
7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do
each of the following at least once:

• Use a conditional test in the while statement to stop the loop.

• Use an active variable to control how long the loop runs.

• Use a break statement to exit the loop when the user enters a 'quit' value.
"""


# Use a conditional test in the while statement to stop the loop.
topping = ''
while topping != 'quit':
    topping = input("What topping do you want? Enter 'quit' to stop\n---> ")
    if topping != 'quit':
        print(f'Adding {topping} to your pizza')

# Use an active variable to control how long the loop runs.
topping = ''
active = True
while active:
    topping = input("What topping do you want? Enter 'quit' to stop\n---> ")
    if topping == 'quit':
        active = False
    else:
        print(f'Adding {topping} to your pizza')

# Use a break statement to exit the loop when the user enters a 'quit' value
topping = ''
while True:
    topping = input("What topping do you want? Enter 'quit' to stop\n---> ")
    if topping == 'quit':
        break
    else:
        print(f'Adding {topping} to your pizza')
