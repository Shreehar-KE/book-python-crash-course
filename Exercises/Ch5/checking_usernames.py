current_users = ['Indiana Jones', 'John Wick',
                 'Bruce Almighty', 'Sherlock Holmes', 'Jack Sparrow']
current_users_lowercase = [name.lower() for name in current_users]

new_users = ['Gandalf', 'John McClane',
             'john wick', 'Scott Pilgrim', 'Indiana Jones']

for user in new_users:
    if user.lower() in current_users_lowercase:
        print(f'{user} is not available, Enter a new username!')
    else:
        print(f'{user} is available.')
