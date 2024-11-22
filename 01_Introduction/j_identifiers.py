"""

Purpose: Identifiers in python

    Variable
        1. keyword    --> Words which have some meaning in that language
        2. Identifier  -> Words which are defined by user(developers)

Identifiers are user defined variables
"""

# Loading a module

import keyword

print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


print(True) #True

# print(true) NameError: name 'true' is not defined.
#   File "/workspaces/PythonBatchNovDec2024/01_Introduction/j_identifiers.py", line 22, in <module>
#     print(true)
#           ^^^^
# NameError: name 'true' is not defined. Did you mean: 'True'?


my_value = 'something'
print(my_value) #Identifier

#True = 'something'
#     True = 'something'
#     ^^^^
# SyntaxError: cannot assign to True


print(keyword.iskeyword("True"))       #True
print(keyword.iskeyword("true"))       #False
print(keyword.iskeyword("my_value"))   #False



# ----------------------------------------
# Identifiers - user-defined variables
#     - Naming Convention
#         1. keywords should not be used as identifiers
#         2. first character: a-z, A-Z, __annotations__
#         3. remaining chars: a-z, A-Z, _, 0-9

# -------- Rule 1
# True = 123 # SyntaxError: cannot assign to True
# None = 'Nothing' # SyntaxError: cannot assign to None

# PEP 8 - Dont create identifiers which are similar to your keywords
true = 123
none = 'Nothing'

true_value = 123
none_result = 'Nothing'


# ---- Rule 2 & 3

name = 'Priyanka'
name_of_student = 'Priyanka'
first_name = 'Priyanka'
student_1 = 'Priyanka'
Class_o2_a = 'Python comment operations'
first____Child = 'Suleman'

#  PEP 8 recommands to use the capitals for constants

PI = 3.1416
DOZEN = 12

# $name = 'Priyanka'
# name-of-student = 'Priyanka'
# name of student = 'Priyanka'
# 1st_name = 'Priyanka'


_2nd_student = 'someone'

_job = "software Developer"
__role = "Product Support"
___salary = 1233456773846874



# OOP -> name mangling
# variable   -> Public variable
# _variable  -> Protected variable
# __variable -> Private variable

#  __variable__ -> Built-in function
# Ex:  __file__, __name__, __doc__, __dict__, __init__    ---dunder menthods, double underscore methods, magic methods


print("__name__", __name__) # __main__ 
print("__file__", __file__) # file path /workspaces/PythonBatchNovDec2024/01_Introduction/j_identifiers.py


# print("__Suleman__", __Suleman__)
# NameError: name '__Suleman__' is not defined