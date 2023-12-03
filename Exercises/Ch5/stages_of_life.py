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
