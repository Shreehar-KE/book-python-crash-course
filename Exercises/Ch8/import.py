"""
8-16. Imports: Using a program you wrote that has one function in it, store that
function in a separate file. Import the function into your main program file, and
call the function using each of these approaches:

import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
"""


import simple_module
from simple_module import another_function
from simple_module import simple_function as sf
import simple_module as sm
from simple_module import *


simple_module.simple_function()
another_function()
sf()
sm.another_function()
simple_function()
