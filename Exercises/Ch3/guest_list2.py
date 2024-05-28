"""
3-5. Changing Guest List: You just heard that one of your guests can't make the
dinner, so you need to send out a new set of invitations. You'll have to think of
someone else to invite.

• Start with your program from Exercise 3-4. Add a print() call at the end of
  your program, stating the name of the guest who can't make it.

• Modify your list, replacing the name of the guest who can't make it with the
  name of the new person you are inviting.

• Print a second set of invitation messages, one for each person who is still in
  your list.
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
