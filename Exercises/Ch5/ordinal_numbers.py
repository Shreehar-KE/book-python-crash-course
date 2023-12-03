num_list = [num for num in range(1, 10)]

for num in num_list:
    suffix = 'th'
    if num == 1:
        suffix = 'st'
    elif num == 2:
        suffix = 'nd'
    elif num == 3:
        suffix = 'rd'
    print(f'{num}{suffix}')
