Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Define the function to compare two numbers
>>> def greater_than(x,y):
...     if x > y:
...         return True
...     else:
...         return False
... 
...     
>>> # Main section
>>> a = 2
>>> b = 3
>>> 
>>> #Call the function for the result
>>> result = greater_than (a,b)
>>> 
>>> #Print the output
>>> print("The statement " = str(a) + "is greter than " + str(b) + "is " + str(result))
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
SyntaxError: invalid syntax
>>> print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))
The statement 2 is greater than 3 is False
>>> 
>>> # Main section
>>> a = 10
>>> b = 6
>>> 
>>> # Call the function for the result
>>> result = greater_than(a,b)
>>> 
>>> print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))
The statement 10 is greater than 6 is True
