dream_vacation = {}
prompt = 'If you could visit one place in the world, where would you go?\n---> '
while True:
    name = input('\nEnter your name: ')
    place = input(prompt)
    dream_vacation[name] = place
    repeat = input("\nWould you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        break

print("\n--- Poll Results ---")
for name, response in dream_vacation.items():
    print(f"{name} would like to visit {response}.")
