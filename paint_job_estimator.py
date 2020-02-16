# Joshua Torain CIS-115 FON04
# write a main function to control logic
# create two functions for user input. one to get the square footage and one to get the price per gallon of the paint
# create functions to calculate the number of hours of labor needed, gallons of paint needed
# the total labor charges, the cost of the paint, and total cost of the job
# create a function to display the results

# import math to use the math.ceil() function, in order to round the hours of labor and amount of paint needed up to
# the nearest whole number.
import math


# create main function to control the flow of logic
def main():
    user_square_feet = square_feet()
    user_price_of_paint = price_of_paint()
    hours_of_labor = calculate_hours_of_labor(user_square_feet)
    gallons_of_paint_needed = calculate_gallons_of_paint_needed(user_square_feet)
    cost_of_paint = calculate_cost_of_paint(gallons_of_paint_needed, user_price_of_paint)
    labor_charges = calculate_labor_charges(hours_of_labor)
    total_cost = calculate_total_cost(cost_of_paint, labor_charges)
    display_results(gallons_of_paint_needed, hours_of_labor, cost_of_paint, labor_charges, total_cost)


# function to get user input for amount of square footage
def square_feet():
    # create variable with user input. store as float
    user_square_feet = float(input('How much square feet of wall space do you have? '))
    # return the variable
    return user_square_feet


# function to get user input for price of paint per gallon
def price_of_paint():
    # create variable with user input. store as float
    user_price_of_paint = float(input('What is the price of your paint per gallon? '))
    # return the variable
    return user_price_of_paint


# function to calculate hours of labor required. Use square footage from user as parameter
def calculate_hours_of_labor(user_square_feet):
    # create formula to find number of hours or labor needed. Store as variable. 
    hours_of_labor = user_square_feet/112 * 8
    # return the variable
    return hours_of_labor


# function to calculate amount of paint needed. use square footage as parameter
def calculate_gallons_of_paint_needed(user_square_feet):
    # create formula to calculate the number of gallons needed. store as variable.
    gallons_of_paint_needed = user_square_feet/112
    # return the variable
    return gallons_of_paint_needed


# function to calculate the cost of paint. Use gallon of paint needed and price of paint as parameters
def calculate_cost_of_paint(gallons_of_paint_needed, user_price_of_paint):
    # create formula to find the total cost of paint. Store as variable
    cost_of_paint = gallons_of_paint_needed * user_price_of_paint
    # return the variable
    return cost_of_paint


# function to calculate the labor charges. Use the hours of labor needed as parameters
def calculate_labor_charges(hours_of_labor):
    # create formula to calculate the total cost of the labor. Store as a variable
    labor_charges = hours_of_labor * 35
    # return the variable
    return labor_charges


# function to calculate the total cost of the paint job. Use cost of paint and labor charges as parameters
def calculate_total_cost(cost_of_paint, labor_charges):
    # create formula to calulate the total cost of the paint job. store as a variable
    total_cost = cost_of_paint + labor_charges
    # return the variable
    return total_cost


# function to display the resuls to the user. use previous variables as parameters. format costs in dollars. use math.ceil to round up
def display_results(gallons_of_paint_needed, hours_of_labor, cost_of_paint, labor_charges, total_cost):
    print('You need', math.ceil(gallons_of_paint_needed), 'gallons of paint.')
    print('This will require', math.ceil(hours_of_labor), 'hours of labor.')
    print('The total cost of the paint is $', format(cost_of_paint, ',.2f'))
    print('The labor charges are $', format(labor_charges, ',.2f'))
    print('The total cost of the job is $', format(total_cost, ',.2f'))


# call the main function
main()
