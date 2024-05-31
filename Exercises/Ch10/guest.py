"""
10-4. Guest: Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.
"""


from pathlib import Path
name = input('Enter your name: ')
path = Path('guest.txt')
path.write_text(name)
