guests = ['Steve Jobs', 'APJ Abdul Kalam', 'Archimedes']
print(f'Dear {guests[0]}, I cordially invite you to a dinner.')
print(f'Dear {guests[1]}, I cordially invite you to a dinner.')
print(f'Dear {guests[2]}, I cordially invite you to a dinner.')

print(f"\n{guests[2]} won't be attending the Dinner.\n")

guests[2] = "Leonardo Da Vinci"
print(f'Dear {guests[0]}, I cordially invite you to a dinner.')
print(f'Dear {guests[1]}, I cordially invite you to a dinner.')
print(f'Dear {guests[2]}, I cordially invite you to a dinner.')

print('\nI just found a bigger table for the Dinner...!\n')
guests.insert(0, 'Mubasil')
guests.insert(2, 'Santha')
guests.append('Thaha')
print(f'Dear {guests[0]}, I cordially invite you to a dinner.')
print(f'Dear {guests[1]}, I cordially invite you to a dinner.')
print(f'Dear {guests[2]}, I cordially invite you to a dinner.')
print(f'Dear {guests[3]}, I cordially invite you to a dinner.')
print(f'Dear {guests[4]}, I cordially invite you to a dinner.')
print(f'Dear {guests[5]}, I cordially invite you to a dinner.')

print("\nThe new table won't arrive in time for the Dinner, so I can invite only two guests.\n")
print(f'Dear {guests.pop()}, sorry for not inviting to the Dinner.')
print(f'Dear {guests.pop()}, sorry for not inviting to the Dinner.')
print(f'Dear {guests.pop(2)}, sorry for not inviting to the Dinner.')
print(f'Dear {guests.pop(0)}, sorry for not inviting to the Dinner.')

print(f'\nDear {guests[0]}, you are still invited to the Dinner.')
print(f'Dear {guests[1]}, you are still invited to the Dinner.')

del guests[1]
del guests[0]
print(guests)
