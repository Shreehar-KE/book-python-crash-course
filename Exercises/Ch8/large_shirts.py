"""
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.
"""


def make_shirt(size='L', text='I love Python'):
    """prints a message that a shirt has been made as per given size and text"""
    print(f'made a size {size} with text: {text}')


make_shirt()

make_shirt(size='M')

make_shirt(size='S', text='NULL')
