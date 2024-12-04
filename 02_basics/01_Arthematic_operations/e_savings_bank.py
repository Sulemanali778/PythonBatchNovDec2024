"""

Purpose: Saving Bank

    Initial Balance 0

Algorithm
---------
step 1: Create an variable 'balance' with initial value 0
step 2: Initial Deposit of min  balance 1500
step 3: Salary crediated of 3300
step 4: Online Purchase of 33.33
step 5: House Rent paid of 1500
step 6: Display Balance
"""



# Step 1: Create a variable 'balance' with initial value 0
balance = 0
print("Balance at the initial stage is :", balance)

# Step 2: Initial Deposit of min balance 1500
Intital_Deposit = 1500
balance = Intital_Deposit + balance
print("Balance after initial deposit is :", balance)

# Step 3: Salary credited of 3300
Salary_credited = 3300
balance = Salary_credited + balance
print("Balance after salary credited is :", balance)

# Step 4: Online Purchase of 33.33
Online_purchase = 33.33
balance = balance - Online_purchase
print("Balance after online purchase is :", balance)

# Step 5: House Rent paid of 1500
Rent = 1500
balance = balance - Rent
print("Final Balance after paying rent is :", balance)



