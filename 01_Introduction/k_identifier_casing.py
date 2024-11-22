#!/usr/bin/python3
"""

Purpose: Identifier Casing
    PEP(python Enhancement Proposal) 8 - coding style
    - class names should be CamleCase
    - identifier names should be in snake ( or Underscore)

    Article : https://ieeexplore.ieee.org/document/5521745
"""

# Python is case-sentitive language
animal = 'DOG'
print(animal)

# print(Animal)
# NameError: name 'Animal' is not defined. Did you mean: 'animal'?

ANIMAL = 'PIG'
print(ANIMAL)

Animal = 'Camel'
print(Animal)



# -------------
# variable casing
# 1. snake Casing or underscore casing


student = 'suleman'
employee_salary = 23345276.24
cost_of_mango = 12
selling_price_of_apple = 34

output_of_thermal_sensor = 32
no_of_current_processos = 5

# 2. Camel Casing 

student = 'suleman'
EmployeeSalary = 23345276.24
CostOfMango = 12
SellingPriceOfApple = 34

OutputOfThermalSensor = 32
NoOfCurrentProcessos = 5

