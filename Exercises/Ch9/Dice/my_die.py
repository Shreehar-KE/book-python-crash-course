"""
9-13. Dice: Make a class Die with one attribute called sides, which has a
default value of 6. Write a method called roll_die() that prints a random num-
ber between 1 and the number of sides the die has. Make a 6-sided die and
roll it 10 times.

      Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""

import die

my_die = die.Die(6)

print('\n Rolling the 6-sided die 10 times.\n')
for i in range(10):
    my_die.roll_die()

ten_sided_die = die.Die(10)

print('\n Rolling the 10-sided die 10 times.\n')
for i in range(10):
    ten_sided_die.roll_die()

twenty_sided_die = die.Die(20)

print('\n Rolling the 20-sided die 10 times.\n')
for i in range(10):
    twenty_sided_die.roll_die()
