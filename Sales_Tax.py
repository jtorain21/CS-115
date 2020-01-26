# Joshua Torain CIS-115 FON04

# pseudocode
# ask the user for the amount of their purchase
# calculate the state sales tax
# calculate the county sales tax
# calculate the total sales tax
# calculate the total sum of the amount of purchase plus sales tax
# Display all values to the user

# Ask ther user for the amount of their purchase
pre_tax_puchase_amount = float(input('How much was your purchase?'))

# Calculate the state sales tax, which is 5 percent
state_sales_tax = pre_tax_puchase_amount * 0.05

# Calculate the county sales tax, which is 2.5 percent
county_sales_tax = pre_tax_puchase_amount * 0.025

# Calculate the total sales tax
total_sales_tax = state_sales_tax + county_sales_tax

# Calculate the total sum of the amount of purchase plus sales tax
total_purchase_plus_sales_tax = total_sales_tax + pre_tax_puchase_amount

# Convert values into dollars
state_sales_tax_in_dollars = format(state_sales_tax, ',.2f')
county_sales_tax_in_dollars = format(county_sales_tax, ',.2f')
total_sales_tax_in_dollars = format(total_sales_tax, ',.2f')
total_purchase_plus_sales_tax_in_dollars = format(total_purchase_plus_sales_tax, ',.2f')

# Display all values to the user
print('The state sales tax is $', state_sales_tax_in_dollars)
print('The county sales tax is $', county_sales_tax_in_dollars)
print('The total sales tax is $', total_sales_tax_in_dollars)
print('The total cost of the purchase plus tax is $', total_purchase_plus_sales_tax_in_dollars)
