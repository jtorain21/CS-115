# Joshua Torain CIS-115 FON04

# pseudocode
# Step 1 Ask the user to input what their projected total sales will be
# Take input from step 1 and convert it into a floating point number
# Calculate the profit, which is 23% of the total sales
# Display the profit to the user


# Get the projected total sales from user
projected_total_sales = float(input('What do you project your total sales to be?'))

# Calculate the profit, which is 23% of the total sales
profit = projected_total_sales * 0.23

# Convert profit to dollars, using format
profit_in_dollars = format(profit, ',.2f')

# Display the profit to the user.
print('Your projected profit is $', profit_in_dollars)
