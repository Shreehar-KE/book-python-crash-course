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
