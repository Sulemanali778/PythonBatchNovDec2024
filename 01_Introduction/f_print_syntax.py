#!/usr/bin/python3
"""

Purpose: print() function syntax and usage
"""

name = "Almighty"  #str

print("name =", name)
print("name of the student is name")


#       str             str

print("name of the student is " + name)


print("name of the student is", name)
print("name of the student is", name, sep=" ")
print("name of the student is", name, sep="-")
print("name of the student is", name, sep="")


print(1, 2, 3, 4, 5, 6) # default sep=
print(1, 2, 3, 4, 5, 6, sep=" ")
print()


print(1, 2, 3, 4, 5, 6, sep="~")
print(1, 2, 3, 4, 5, 6, sep="_")
print(1, 2, 3, 4, 5, 6, sep=":")
print()


# python is dynamically typed language

num1 = 123
print("Name of student is", num1)


#           str             int

#print("Name of student is" + num1)
"""
Name of student is 123
Traceback (most recent call last):
  File "./f_print_syntax.py", line 43, in <module>
    print("Name of student is" + num1)
TypeError: can only concatenate str (not "int") to str
"""

#Note: python is a strictly typed language

print('1 + 2 =', 1+2) #addition
print("'1' '2' =", "1" + "2") # string concatination
print()


#1 + '2' # typeError: unsupported operand type(s) for += 'int' and 'str'
# type converters - str(), int(), float()

print("1 + int('2')=", 1, int('2'))
print("str(1) + '2'=", str(1), '2')

print()
print("int('123)    =", int("123"))


print("int(23.4) =", int(23.4)) # ValueError: invalid identifier
#print("int(two) =", int(two))   # ValueError: invalid identifier


print("name of student is" + str(num1))
print("name of student is" + " " + str(num1))
