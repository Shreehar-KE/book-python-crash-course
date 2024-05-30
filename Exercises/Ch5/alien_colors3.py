"""
5-5. Alien Colors #3: Turn your if- else chain from Exercise 5-4 into an if- elif-
else chain.

• If the alien is green, print a message that the player earned 5 points.

• If the alien is yellow, print a message that the player earned 10 points.

• If the alien is red, print a message that the player earned 15 points.

• Write three versions of this program, making sure each message is printed
  for the appropriate color alien.
"""


alien_color1 = 'green'

if alien_color1 == 'green':
    print('You have earned 5 points.')
elif alien_color1 == 'yellow':
    print('You have earned 10 points.')
else:
    print('You have earned 15 points.')

# Version 2

alien_color2 = 'yellow'

if alien_color2 == 'green':
    print('You have earned 5 points.')
elif alien_color2 == 'yellow':
    print('You have earned 10 points.')
else:
    print('You have earned 15 points.')

# Version 3

alien_color3 = 'red'

if alien_color3 == 'green':
    print('You have earned 5 points.')
elif alien_color3 == 'yellow':
    print('You have earned 10 points.')
else:
    print('You have earned 15 points.')
