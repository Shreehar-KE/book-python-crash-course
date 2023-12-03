usernames = []
# usernames = ['Indiana Jones', 'John Wick','Bruce Almighty', 'admin', 'Jack Sparrow']

if usernames:
    for username in usernames:
        if username == 'admin':
            print(f'Hello {username}, would you like to see a status report?')
        else:
            print(f'Hello {username}, thank you for logging in again.')
else:
    print('We need to find some users!')
