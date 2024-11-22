#!/usr/bin/python3
"""
Purpose: Working with Multi-line statements

    Python is a interpreter-based language
    -Each line executes seperatly
    - \ line contiuantion operator or reverse division which was used in python 2
    - Will join more than one line to a single statement


Brace
    () Paranthesis

    [] square braces
    {} flower braces


PEP 8 :
    a) Lines should be 79 characters in length or less
    b) Continuations of long expression onto additional lines should be
    indented by four extra spaces from their normal identation level.
"""






sum_of_values = 123 + 23 - 123 * 2 / 12
print(sum_of_values)


sum_of_values = 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12 * 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12 * 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12 / 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12
print(sum_of_values)


sum_of_values = 123 + 23 - 123 * 2 \
/ 12 - 123 + 23- 123 * 2 / 12 - 123 + 23 \
- 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12 - 123 \
+ 23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12 \
* 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 \
/ 12 * 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 \
* 2 / 12 - 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 \
    * 2 / 12 / 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12
print(sum_of_values)


# Braces alongside line continuation operator

sum_of_values = (123 + 23 - 123 * 2 \
/ 12 - 123 + 23- 123 * 2 / 12 - 123 + 23 \
- 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12 - 123 \
+ 23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12 \
* 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 \
/ 12 * 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 \
* 2 / 12 - 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 \
    * 2 / 12 / 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12)
print(sum_of_values)



# Braces alone

sum_of_values = (123 + 23 - 123 * 2 
/ 12 - 123 + 23- 123 * 2 / 12 - 123 + 23 
- 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12 - 123 
+ 23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12 
* 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 
/ 12 * 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 
* 2 / 12 - 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 
    * 2 / 12 / 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12)
print(sum_of_values)



# Square Braces alone -- list in the python

sum_of_values = [123 + 23 - 123 * 2 
/ 12 - 123 + 23- 123 * 2 / 12 - 123 + 23 
- 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12 - 123 
+ 23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12 
* 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 
/ 12 * 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 
* 2 / 12 - 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 
    * 2 / 12 / 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12]
print(sum_of_values)


# Flower Braces alone

sum_of_values = {123 + 23 - 123 * 2 
/ 12 - 123 + 23- 123 * 2 / 12 - 123 + 23 
- 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12 - 123 
+ 23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12 
* 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 
/ 12 * 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 
* 2 / 12 - 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 
    * 2 / 12 / 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12}
print(sum_of_values)



