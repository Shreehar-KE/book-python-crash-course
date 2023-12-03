topping = ''

while topping != 'quit':
    topping = input("What topping do you want? Enter 'quit' to stop\n---> ")
    if topping != 'quit':
        print(f'Adding {topping} to your pizza')
