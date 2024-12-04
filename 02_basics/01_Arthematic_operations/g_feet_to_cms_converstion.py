"""
Purpose: Feet to Centimeters converstion

    1 foot = 12 inches
    1 inch = 2.54 cms

    
Algorithm:
----------
Step 1: Get feet values in runtime
step 2: compute feet to cms
            feet to inches, then
            inches to cms
Step 3: Display the results

"""


Feet = float(input("Enter the number in feets: "))

Inches = 12 * Feet

Centimeter = 2.54 * Inches

print("Number in Centimeters =", str(Centimeter), 'CMS')