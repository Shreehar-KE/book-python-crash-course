"""
3-7. Shrinking Guest List: You just found out that your new dinner table won't
arrive in time for the dinner, and now you have space for only two guests.

• Start with your program from Exercise 3-6. Add a new line that prints a
  message saying that you can invite only two people for dinner.

• Use pop() to remove guests from your list one at a time until only two
  names remain in your list. Each time you pop a name from your list, print a
  message to that person letting them know you're sorry you can't invite them
  to dinner.

• Print a message to each of the two people still on your list, letting them
  know they're still invited.

• Use del to remove the last two names from your list, so you have an empty
  list. Print your list to make sure you actually have an empty list at the end of
  your program.
"""

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
