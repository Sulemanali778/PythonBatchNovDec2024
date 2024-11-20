#!/usr/bin/python3
"""
Purpose: Basic PEP 8 Guidelines and 
        shebang linech

    PEP - python Enhancement Proposal
    PEP 8 - coding style guide 
This is Doc String

"""

# print as a statement in python 2
#print "Hello World!"

# print as function in python 3

print('Hello World')
print(True)
print("True", 123, None)


def wishes(name):
    wish = "How are you {0}?".format(name)
    print(wish)

wishes("Suleman")