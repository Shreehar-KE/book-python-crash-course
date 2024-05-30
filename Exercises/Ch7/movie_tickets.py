"""
7-5. Movie Tickets: A movie theater charges different ticket prices depending on
a person's age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.
"""


print('Welcome to Py Cinemas Ticket Counter, Enter 0 to quit')
while True:
    age = int(input('Enter your age: '))
    if age == 0:
        break
    elif age < 3:
        print('Ticket is free for you..!')
    elif age <= 12:
        print('A Ticket is $10 for you')
    else:
        print('A Ticket is $15 for you')
