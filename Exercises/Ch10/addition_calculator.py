"""
10-7. Addition Calculator: Wrap your code from Exercise 10-5 in a while loop
so the user can continue entering numbers, even if they make a mistake and
enter text instead of a number.
"""


while True:
    print("\nEnter 'q' to quit anytime...!")
    num1 = input('Enter 1st number: ')
    num2 = input('Enter 2nd number: ')

    if num1 == 'q' or num2 == 'q':
        break

    try:
        sum = int(num1) + int(num2)
    except ValueError:
        print('Enter numerical values only...!')
    else:
        print(sum)
