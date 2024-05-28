"""
3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.

• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
  end of your program, informing people that you found a bigger table.

• Use insert() to add one new guest to the beginning of your list.

• Use insert() to add one new guest to the middle of your list.

• Use append() to add one new guest to the end of your list.

• Print a new set of invitation messages, one for each person in your list.
"""

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
