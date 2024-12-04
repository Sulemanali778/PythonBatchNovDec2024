"""

Purpose: Ration Store


    ------------------------------------------------------------
    item        cost        Quantity        Amount
    ------------------------------------------------------------
    wheat       25/kg       30 kgs          25 * 30 = 750/-
    Rice        12/kg       50 kgs          12 * 50 = 600/-
                                        ------------------------
                                                      1350/-
                                        subsidy 20%   -270/-
                                        ------------------------
                                        BillableAmount:1080/-

Algorithm
---------
Step 1: Get the cost of items into variables
step 2: Get the quantity of iteams into variables
step 3: Compute the selling price to each iteam,
        and add them
step 4: Compute the subsidy amount and subtract
        from the selling price
step 5: Display the billable amount

"""

# cost of items
cost_of_wheat = 25
cost_of_rice = 12

#Quantity of items
qty_of_wheat = 30 # kgs
qty_of_rice = 50 # kgs

# Selling Price computation
sp_of_wheat = cost_of_wheat * qty_of_wheat
sp_of_rice = cost_of_rice * qty_of_rice

total_sp = sp_of_wheat + sp_of_rice

print("Total Selling Price = ",total_sp)


# Subsidy calculation at 20% subsidy
subsidy_amount = (total_sp * 20) / 100  # Pemdas

print("Subsidy Amount = ", subsidy_amount)


billable_amount = total_sp - subsidy_amount


print("Billable Amount : ", billable_amount)