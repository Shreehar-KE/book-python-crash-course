"""
5-6. Stages of Life: Write an if- elif- else chain that determines a person's stage
of life. Set a value for the variable age, and then:
84
Chapter 5
•If the person is less than 2 years old, print a message that the person is
a baby.
•If the person is at least 2 years old but less than 4, print a message that the
person is a toddler.
•If the person is at least 4 years old but less than 13, print a message that
the person is a kid.
•If the person is at least 13 years old but less than 20, print a message that
the person is a teenager.
•If the person is at least 20 years old but less than 65, print a message that
the person is an adult.
•If the person is age 65 or older, print a message that the person is an elder.
"""


age = 2

if age < 2:
    msg = 'a baby'
elif age < 4:
    msg = 'a toddler'
elif age < 13:
    msg = 'a kid'
elif age < 20:
    msg = 'a teenager'
elif age < 65:
    msg = 'an adult'
elif age >= 65:
    msg = 'an elder'

print(f'The person is {msg}.')
