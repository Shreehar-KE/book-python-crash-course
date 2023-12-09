# Chapter 2: Variables and Simple Data Types

* What Really Happens When You Run hello_world.py
* Variables
* Strings
* Numbers
* Comments
* The Zen of Python

#### What Really Happens When You Run hello_world.py

* Python Interpreter
* Syntax Highlighting

#### Variables
* Variable & Value
* Traceback
* name error
* Variables are labels

#### Strings
* Series of characters
* Anything inside quotes
* Single or Double quotes
* `str.title()` method
* Dot (.) Operator
* `str.upper()` method
* `str.lower()` method
* f-strings (f : format)
  * `f"Using a variable {var} inside a String"`
* Whitespace characters: space, \n, \t
* `str.strip()`, `str.lstrip()`, `str.rstrip()` methods
* `url.removeprefix('https://')` method
* Syntax Errors
* `filename.removesuffix('.txt')` method

#### Numbers
* Integer
* Arithmetic Operators: + - * / ** 
* Operator Precedence, ()
* Float
  * `0.2 + 0.1 = 0.30000000000000004`
  * `4 / 2 = 2.0`
* Underscores to group digits
  * `universe_age = 14_000_000_000`
  * `print(universe_age) # 14000000000`
* Multiple Assignment
* Constants (not built-in python)

#### Comments
* Meaningful comments

---

# Chapter 3: Introducing Lists

* What is a List?
* Modifying, Adding, and Removing Elements
* Organizing a List
* Avoiding Index Errors When Working with Lists

#### What is a List?
* [], separated by commas, can be unrelated
* Index, starts from 0
* `sample_list[-1]` to access the last element

#### Modifying, Adding, and Removing Elements
* Lists are dynamic(size)
* `sample_list.append(value)` method
* `sample_list.insert(pos, val)` method
* `del sample_list[pos]` method
  * permanently deletes the item at pos
* `removed_item = sample_list.pop()` method
  * return the last item and removes it from the list
* `some_item = sample_list.pop(pos)` method
  * return the item at pos and removes it from the list
* `sample_list.remove(value)` 
  * removes the item by its value
  * first appearance only

#### Organizing a list
* `list.sort()` method
  * changes the order permanently
* `list.sort(reverse=True)` method
* `sorted(list)` function
  * doesn't modify the list
  * also accepts `reverse=True` argument
* `list.reverse()` method
  * reverses the original order, permanently modifies the list
* `len(list)` function
  * returns the length of the list, i.e no. of items

---

# Chapter 4: Working with Lists

* Looping Through an Entire List
* Avoiding Indentation Errors
* Making Numerical Lists
* Working with Part of a List
* Tuples
* Styling Your Code

#### Looping Through an Entire List
* for loop

#### Avoiding Indentation Errors
* Indentation 
* Indentation Errors
* Logical Error

#### Making Numerical Lists
* `range(start,end,step)` function
  * `range(1,5)` means 1 to 4
  * `range(5)` means 0 to 5
* `list()` function
  * `list(range(5))` : [0,1,2,3,4]
* `min(num_list)` function
* `max(num_list)` function
* `sum(num_list)` function
* List comprehension
  * ex: `squares = [value**2 for value in range(1,11)]`

#### Working with Part of a List
* List slicing (:)
* `sample_list[start:end:step]`
* `sample_list = another_list[:]` copy without reference

#### Tuples
* immutable
* ()
* `tup = (1,)` include trailing comma for tuple with 1 element

---

# Chapter 5: If Statements

* A Simple Example
* Conditional Tests
* if Statements
* Using if Statement with Lists
* Styling Your if Statements

#### Conditional Tests
* Equality operator
* Inquality operator
* < > <= >=
* and   or
* in    not in
* Boolean Values & Expressions

#### if Statements
* Simple if statement
* if-else block
* if-elif-else chain
* omitting the else block
* nested-if statement

#### Using if statements with Lists
* Checking That a List Is Not Empty 
  
    ```python
        requested_toppings = []
        if requested_toppings:
            for requested_topping in requested_toppings:
                print(f"Adding {requested_topping}.")
            print("\nFinished making your pizza!")
        else:
            print("Are you sure you want a plain pizza?")
    ```

---

# Chapter 6: Dictionaries

* A Simple Dictionary
* Working with Dictionaries
* Looping through a Dictionary
* Nesting

#### Working with Dictionaries
* {key:value,...}
* To access a value in a dictionary
  * `sample_dict[key]`
* Dynamic data structures
* To remove key-value pairs
  * `del sample_dict[key]`
* `sample_dict.get(key)` method
  * returns 'None' or the default value passed as a parameter if the key doesn't exists.

#### Looping through a Dictionary
* `for key,value in dict_1.items():`
  * to loop through each key-value pair for each iteration
* `for key in dict_1.keys():`
  * same as `for key in dict_1:`
  * `if key in dict_1.keys():`
* `for value in dict_1.values():`
* `set(dict_1.values)` to get unique values
  * set : `{value1, value2}`

---

# Chapter 7: User Input and While Loops

* How the input() Function works
* Introducing while Loops
* Using a while Loop with Lists and Dictionaries

#### How the input() Function works
* prompt argument 
  * can be a string variable also
* int() function
* % operator

#### Introducing while Loops
* flag variable
* break statement
* continue statement

#### Using a while Loop with Lists and Dictionaries
* provides the ability to modify the list while looping

---

# Chapter 8: Functions

* Defining a Function
* Passing Arguments
* Return Values
* Passing a List
* Passing an Arbitary Number of Arguments
* Storing Your Functions in Modules
* Styling Functions

#### Defining a Function
* Function definition
* docstring `"""descibes what the function does"""`
* parameter - in function definition
* argument - in function call

#### Passing Arguments
* Positional Arguments
* Keyword Arguments
* Default values - for parameters
  * place it after other parameters(wihtout default values)

#### Return Values
* making optional arguments
* `None` value

#### Passing a List
* Reference nature of Lists
* Shallow copying a list to prevent modification 

#### Passing an Arbitary Number of Arguments
* `*` before parameter to create a tuple
* place this parameter at last in the function definition
* `**` before parameter to create a dicitonary

#### Storing Your Functions in Modules
* `import` statement
* `module_name.fuction_name()`
* `from module_name import function_0, function_1`
* `as` keyword - to create alias
* `from module_name import *` to import every function in that modue
  * can each function without dot(.) notation

#### Styling Functions
* Desctiptive function names
* Lowercase letter & underscores
* Docstring comment
* no spaces around equal sign when specifying default value for a parameter.
  * same convention for keyword arguments
* when >79 characters in function definition, after `(` newline and indent the parameters with two tab spaces and place below  
* two blank lines between two functions

---

# Chapter 9: Classes

* Creating and Using a Class
* Working with Classes and Instances
* Inheritance
* Importing Classes
* The Python Standard Library
* Styling Classes

#### Creating and Using a Class
* * A function that’s part of a class is a method.
* `__init__()` method - to initialize attributes
* `self` parameter 
  * required in the method definition
  * must come first before other parameters
  * similar to `this` keyword in `Java`
* attributes - variables associated with instances
* Class ~ set of instructions for how to make an instance
* Object : instance of a class

#### Working with Classes and Instances
* modifying attributes directly, through a method(setter)

#### Inheritance 
* Parent Class and Child Class
* `Class Child(Parent)` 
* `super()` function
* Override Method
  * declare methods with same name
* composition
  * breaking of larger class into smaller classes

#### Importing Classes
* module level docstring
* storing multiple classes in a module
* breaking down a module

#### The Python Standard Library
* `random` module
  * `randint()` function
  * `choice()` function

#### Styling Classes
* CamelCase naming
* Docstrings
  * after class definition
  * on top of each module
* single blank line b/w methods in a class
* imports from std lib comes before imports from a user-defined modules separated by a blank line

---

# Chapter 10: Files and Exceptions

* Reading from a File
* Writing to a File
* Exceptions
* Storing Data

#### Reading from a File
* `pathlib` module, `Path` class
* library - module with specific functionality
* `path.read_text()` method
* method chaining
* Relative & Absolute File paths
* `splitlines()` method
* + operator with strings : concatenation
* `float()` function

#### Writing to a File
* `path.write_text()` method
  * only write strings
  * creates files if doesn't exists
  * overwrites previous content
  * closes the file properly after writing

#### Exceptions
* Exceptions : errors that arise during a program's execution
  * exception object
* try-except block
* else block
* encoding argument
* `pass` statement

#### Storing Data
* JSON format
* `json` module
* `json.dumps()` and `json.loads()`
* `exists()` method
* refactoring

---

# Chapter 11: Testing Your Code

* Installing pytest with pip
* Testing a Function
* Testing a Class

#### Installing pytest with pip
* To update any third-party package
  * `python3 -m pip install --upgrade package_name`
* To install any third-party package
  * `python3 -m pip install --user package_name`

#### Testing a Function
* Unit test
* Test case
* Naming a test file: `test_`
* Assertion
* dot indicator 

#### Testing a Class
* commonly used assertion station
* fixture
  * `@pytest.fixture`
* decorator

---