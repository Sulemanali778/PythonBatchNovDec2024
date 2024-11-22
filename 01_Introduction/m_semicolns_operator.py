#!/usr/bin/python3

"""

Purpose: Multiple statements in same line
    , logic seperator
    ; statement completion operator
"""


print("Hello" "World")
print("Hello","World")

print("Hello",12345)
# print("hello" 23135)
# SyntaxError: invalid syntax. Perhaps you forgot a comma?

print("hello", 2312, 213, 123 + 123 - 3)
print()


# semicoln operator


# Method 1

num1 = 100
num2 = 200
sum_of_numbers = num1 + num2
print("Sum_of_number:", sum_of_numbers)


# Method 2

num1 = 100; num2 = 200; sum_of_numbers = num1 + num2; print("Sum_of_number:", sum_of_numbers)



# Conclusion 
# 1. ; is optional. will not change anything 
# 2. ; is important if we need write more than one statement in same
# 3. Unnecessarily placing semicoln at end of statement will increase 


"""

Python -c "print('Hello World')"

python -c "num1 = 100; num2 = 200; sum_of_numbers = num1 + num2; print("Sum_of_number:", sum_of_numbers)"

Language 
    -scripting language Ex: batch, shell,...
    -General Purpose programing language Ex: c, c++, java,...


python is both scripting and General purpose programming Language

.bat
    cd dirctory1
    cd subdirctory2
    ping google.com > result.txt
"""


