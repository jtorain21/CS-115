# Joshua Torain CIS-115 FON04

# write a main function to control logic
# write a function to ask the user for the amount of their purchase
# write a function to calculate the state sales tax
# write a function to calculate the county sales tax
# write a function to calculate the total sales tax
# write a function to calculate the total sum of the amount of purchase plus sales tax
# write a function that Displays all values to the user

# Ask ther user for the amount of their purchase


# write main function
def main():
    user_purchase_amount = purchase_amount()
    state_sales_tax = calculate_state_sales_tax(user_purchase_amount)
    county_sales_tax = calculate_county_sales_tax(user_purchase_amount)
    total_sales_tax = calculate_total_sales_tax(state_sales_tax, county_sales_tax)
    final_sale_amount = calculate_final_sale_amount(user_purchase_amount, total_sales_tax)
    display_results(user_purchase_amount, state_sales_tax, county_sales_tax, total_sales_tax, final_sale_amount)


# function to get user input purchase amount
def purchase_amount():
    # create variable with users input. Store as a float.
    user_purchase_amount = float(input('How much was your purchase? '))
    # return the variable
    return user_purchase_amount


# function to calculate the state sales tax. Use the purchase amount entered by user as parameter
def calculate_state_sales_tax(user_purchase_amount):
    # create variable to store state sales tax
    state_sales_tax = user_purchase_amount * 0.05
    # return the variable
    return state_sales_tax


# function to calculate county sales tax. Again use purchase amount as parameter
def calculate_county_sales_tax(user_purchase_amount):
    # create variable to store county sales tax
    county_sales_tax = user_purchase_amount * 0.025
    # return the variable
    return county_sales_tax


# function to calculate total sales tax. State and county sales tax are parameters
def calculate_total_sales_tax(state_sales_tax, county_sales_tax):
    # create total sales tax variable
    total_sales_tax = state_sales_tax + county_sales_tax
    # return variable
    return total_sales_tax


# function to calculate the final sale amount. Purchase amount and total tax are parameters
def calculate_final_sale_amount(user_purchase_amount, total_sales_tax):
    # create final sale amount variable
    final_sale_amount = user_purchase_amount + total_sales_tax
    # return variable
    return final_sale_amount


# display function. Use all previous variables as parameters.  Format them in dollars with two places after decimal
def display_results(user_purchase_amount, state_sales_tax, county_sales_tax, total_sales_tax, final_sale_amount):
    print('The state sales tax is $', format(state_sales_tax, ',.2f'))
    print('The county sales tax is $', format(county_sales_tax, ',.2f'))
    print('The total sales tax is $', format(total_sales_tax, ',.2f'))
    print('The total cost of the purchase plus tax is $', format(final_sale_amount, ',.2f'))


# call the main function
main()
