"""

Purpose: Bank Loan

        simple interest : A = p(1+rt)

                            A   =   Final Amount
                            p   =   initial principal balance
                            r   =   annual interest rate
                            t   =   time (in years)

Ref : https://www.calculatorsoup.com/calculators/financial/simple-interest-plus-principal-calculator.php
"""





# Simple Interest formula: A = p(1 + rt)

# Input: Initial principal balance (p), annual interest rate (r), and time (t) in years
p = float(input("Enter the initial principal balance for SI: "))
r = float(input("Enter the annual interest rate for SI : "))
r = r / 100
t = float(input("Enter the time (t) in years for SI : "))

# Calculate the final amount (A)
A_SI = p * (1 + r * t)
print("Final Amount of SI :", round(A_SI, 2))

SI = A_SI - p
print("Interest for SI :", round(SI,2))








# Assignment 
# 1. Compound Interest Calculation
#       ref : https://www.calculatorsoup.com/calculators/financial/compound-interest-calculator.php



# Input values for principal, annual interest rate, compounding periods, and time
P = float(input("Enter the principal amount for CI : "))
R = float(input("Enter the annual interest rate for CI : "))
R = R /  100
n = int(input("Enter the number of compounding periods per year for CI : "))
T = float(input("Enter the time in years (t) for CI : "))



# Calculate the final amount (A)
A_CI = P * (1 + r / n) ** (n * t)
print("Final Amount of CI :", round(A_CI, 2))

# Calculate the interest amount (I)
CI = A_CI - P
print("Total Interest Earned (I) for CI:", round(CI,2))


