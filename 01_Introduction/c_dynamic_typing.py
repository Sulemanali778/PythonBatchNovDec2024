#!/usr/bin/python3

"""

Purpose: Python is a dynamic Typed Language.
        Programming Language
            - Classification
                1. Static-Typed Languages
                    -First declare the variables, &
                    -then use them
                        int a, float b #Declaration
                        a = 10         #Initilizing

                2. Dyanamic Typed Languages
                    - Create when you need. No Declaration needed.
                        num1 = 123
                    - line or block based execution

    python code -> python byte code -> pythonInterpreter -> C Complier -> mechine 
    python is slower compared to complier based Languages

"""

num1 = 123
type(num1)

print(type(num1))

print(num1)
print("num1")

print("num1", num1)
print("num1 =", num1)
print("num1 =", num1, "type(num1) =", type(num1))

#works in both static and dynamic typing
num1 = 300
print("num1 =", num1, "type(num1) =", type(num1))#int


#python is dynamic-typed
num1 = 300.0
print("num1 =", num1, "type(num1) =", type(num1))#float


num1 = 300.
print("num1 =", num1, "type(num1) =", type(num1))#float


num1 = 300,
print("num1 =", num1, "type(num1) =", type(num1))#tuple


num1 = (300,)
print("num1 =", num1, "type(num1) =", type(num1))#tuple


num1 = -0.09
print("num1 =", num1, "type(num1) =", type(num1))#float


num1 = -0.09j
print("num1 =", num1, "type(num1) =", type(num1))#complex


num1 = "300"
print("num1 =", num1, "type(num1) =", type(num1))#string


num1 = "Three"
print("num1 =", num1, "type(num1) =", type(num1))#string


num1 = True
#num1 = true #python is case-sensitive language
print("num1 =", num1, "type(num1) =", type(num1))#Boolean


num1 = False
print("num1 =", num1, "type(num1) =", type(num1))#Boolean

num1 = None
print("num1 =", num1, "type(num1) =", type(num1))#none

num1 = "None"
print("num1 =", num1, "type(num1) =", type(num1))#string

num1 = "none"
print("num1 =", num1, "type(num1) =", type(num1))#string

# Note strings need to be declared in quotes
