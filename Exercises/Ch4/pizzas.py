"""
4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
pizza names in a list, and then use a for loop to print the name of each pizza.

• Modify your for loop to print a sentence using the name of the pizza,
  instead of printing just the name of the pizza. For each pizza, you should
  have one line of output containing a simple statement like I like pep-
  peroni pizza.

• Add a line at the end of your program, outside the for loop, that states
  how much you like pizza. The output should consist of three or more lines
  about the kinds of pizza you like and then an additional sentence, such as
  I really love pizza!
"""

pizzas = ['New York Style', 'Neapolitan', 'Sicilian']

for pizza in pizzas:
    print(f'I like {pizza} pizza.')

print('\nNew York-style pizza is large, hand-tossed thin crust. Sold in big slices.')
print('\nNeapolitan pizza is made with tomatoes and mozzarella cheese. The tomatoes must be either San Marzano tomatoes or Pomodorino del Piennolo del Vesuvio.')
print('\nSicilian pizza provides a thick cut of pizza with pillowy dough, a crunchy crust, and robust tomato sauce.')
print('\nI really love pizza!')
