guests = ['Steve Jobs', 'APJ Abdul Kalam', 'Archimedes']
print(f'Dear {guests[0]}, I cordially invite you to a dinner.')
print(f'Dear {guests[1]}, I cordially invite you to a dinner.')
print(f'Dear {guests[2]}, I cordially invite you to a dinner.')

print(f"\n{guests[2]} won't be attending the dinner.\n")

guests[2] = "Leonardo Da Vinci"
print(f'Dear {guests[0]}, I cordially invite you to a dinner.')
print(f'Dear {guests[1]}, I cordially invite you to a dinner.')
print(f'Dear {guests[2]}, I cordially invite you to a dinner.')

print('\nI got reservation to a bigger table...!\n')
guests.insert(0, 'Mubasil')
guests.insert(2, 'Santha')
guests.append('Thaha')
print(f'Dear {guests[0]}, I cordially invite you to a dinner.')
print(f'Dear {guests[1]}, I cordially invite you to a dinner.')
print(f'Dear {guests[2]}, I cordially invite you to a dinner.')
print(f'Dear {guests[3]}, I cordially invite you to a dinner.')
print(f'Dear {guests[4]}, I cordially invite you to a dinner.')
print(f'Dear {guests[5]}, I cordially invite you to a dinner.')
