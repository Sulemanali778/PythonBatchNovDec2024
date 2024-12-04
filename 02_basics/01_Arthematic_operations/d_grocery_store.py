"""

Purpose: Grocery Store

    Item        cost
    -----------------
    rice        10/kg
    wheat       34/kg

Algorithm
----------
step 1: Get the cost of items into variables
step 2: Get the qty of items from user(in run time)

NOTE: input()
        -> to get the value in run-time
        -> will give any input as string only
"""

cost_of_rice = 10  # per kg
cost_of_wheat = 34 # per kg

# Quantities of Items
qty_of_rice = float(input("Enter the Quantity of Rice in KG's :"))
print("Quantity of Rice :", qty_of_rice)

qty_of_wheat = float(input("Enter the Quantity of wheat in KG's :"))
print("Quantity of Wheat :", qty_of_wheat)

# Selling Price computation
sp_of_rice = cost_of_rice * qty_of_rice
print("Selling Price of Rice is :", sp_of_rice)

sp_of_wheat = cost_of_wheat * qty_of_wheat
print("Selling Price of Wheat is :", sp_of_wheat)

total_sp = sp_of_rice + sp_of_wheat
print("Total Selling Price is :", total_sp)