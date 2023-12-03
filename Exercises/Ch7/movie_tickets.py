print('Welcome to Py Cinemas Ticket Counter, Enter 0 to quit')
while True:
    age = int(input('Enter your age: '))
    if age == 0:
        break
    elif age < 3:
        print('Tickets are free for you..!')
    elif age < 12:
        print('A Ticket is $10 for you')
    else:
        print('A Ticket is $15 for you')
