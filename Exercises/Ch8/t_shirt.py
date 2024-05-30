"""
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print a
sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.
"""


def make_shirt(size, text):
    """prints a message that a shirt has been made as per given size and text"""
    print(f'made a size {size} with printed text: {text}')


make_shirt('S', 'One shirt to rule them All')
