#!/usr/bin/python3
"""
Purpose: Print syntax and usage
    Escapes Sequences
        -characters whose presence is felt, but they were not printed
        \t - tab space
        \n - new tab
        \b - overwriting previous character

        r'' - raw string
"""

print("Hello World Python")
print("Hello \tWorld \tPython")
print("Hello \tWorld \nPython")


print()

# To Ignore the escape sequences
print("Hello \tWorld \\nPython")
print(r"Hello \tWorld \nPython")

print("C:\my\newfolder") # noqa: w605
print(r"C:\my\newfolder")
print()



#---
# print(data, sep ='', end = \n)

print('hello') # default end='\n'
print('world')


print ('hello', end="\n")
print ('world', end="\n")


print ('hello', end="____") 
print ('world')  # default end='\n'


print ('hello', end="\t") 
print ('world')  # default end='\n'


print ('hello', 'pthon', 1234, end="\t") 
print ('world')  # default end='\n'


print ('hello', 'pthon', 1234, end="\t", sep=';') 
print ('world')  # default end='\n'