"""
5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

• Look closely at your results, and make sure you understand why each line
  evaluates to True or False.

• Create at least 10 tests. Have at least 5 tests evaluate to True and another
  5 tests evaluate to False.
"""


"""
5-2. More Conditional Tests: You don't have to limit the number of tests you cre-
ate to 10. If you want to try more comparisons, write more tests and add them
to conditional_tests.py. Have at least one True and one False result for each of
the following:

• Tests for equality and inequality with strings

• Tests using the lower() method

• Numerical tests involving equality and inequality, greater than and less
  than, greater than or equal to, and less than or equal to

• Tests using the and keyword and the or keyword

• Test whether an item is in a list

• Test whether an item is not in a list
"""

age = 23
print("Is age > 18? I predict True.")
print(age > 18)
print()

cost_price = 30
selling_price = 38
print("Is it a Loss? I predict False.")
print((selling_price - cost_price) < 0)
print()

discount = 10.0
print("Is the discount more than 10 percent? I predict True.")
print(discount >= 10.0)
print()

count = 16
print("Is the count less than 15? I predict False.")
print(count <= 15)
print()

name = 'Shreehar'
print("Is name == 'shreehar'? I predict True.")
print(name.lower() == 'shreehar')
print()

phone = 'Pixel'
print("Is the phone made by Apple? I predict True.")
print(phone != 'iPhone')
print()

tank_1 = 10
tank_2 = 15
print("Does both the tanks contain more than 15 Litres of Water? I predict False.")
print(tank_1 >= 15 and tank_2 >= 15)
print()

person_1_age = 17
person_2_age = 16
print("Is anyone of the person has the right to vote? I predict False.")
print(person_1_age >= 18 or person_2_age >= 18)
print()

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Is there a '4' in num_list? I predict True.")
print(4 in num_list)
print()


print("Is the list doesn't contain 5? I predict False.")
print(5 not in num_list)
print()
