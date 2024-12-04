"""
Purpose: Fruit Store

    Items       Price       qty                         amount
    ----------------------------------------------------------
    Apples      12/piece    5 dozens = 5 * 12 = 60      12 * 60
    Mangos      34/piece    3 dozens = 3 * 12 = 36      34 * 36
                                                    -----------------
                                                            1944   /-
                                    Discount    2 %         - 38.88/- 
                                                    -----------------
                                                            1905.12/-
                                    GST         +12.5 %     +238.14/-
                                                    -----------------
                                                            2143.26/-


Algorithm
----------
Step 0: Declearing the constants
Step 1: Get the cost of fruits into variables
Step 2: get the qty of fruits into variables
        Compute the end qty, by substituting dozen value.
step 3: Compute the SP to each item and add them
step 4: Compute the Discount Amount and Subtract them fro SP, To create payable amount
step 5: Calculate the GST and add to payable amount, To create billable amount                                                                                                                                                                 
"""


# Constants
DOZEN = 12
DISCOUNT = 2 / 100
GST = 12.5


# Cost of Fruits
cost_of_apple = 12 # per piece
cost_of_mango = 34 # per piece


# Quantity of fruits
qty_of_apples = 5 * DOZEN # Pieces
qty_of_mango  = 3 * DOZEN # pieces

# Selling Price Computation - PEMDAS
total_sp = cost_of_apple * qty_of_apples + cost_of_mango * qty_of_mango
print("Total Selling Price :", total_sp)

# Discount Calculation
discount_amount = total_sp * DISCOUNT
print("Discount Amount :", discount_amount)

# Payable Amount Calculation
payable_amount = total_sp - discount_amount
print("Payable Amount :", payable_amount)

# GST Calulation - PEMDAS
gst_on_fruits = (payable_amount * GST) / 100
print("GST on Fruits :", gst_on_fruits)

# Billable Amount Calculation
billable_amount = payable_amount + gst_on_fruits
print("Billable Amount :", billable_amount)

# round(num, no_of_digits) - function
print("Billable Amount(r) :", round(billable_amount, 2))