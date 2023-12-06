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
