# Joshua Torain CIS 115 FON04
# Design a program that asks the user to enter a store's sales for each day of the week. The amounts should be stored in a list. Use a loop to calculate the total sales for the week and display the result.

# Main() to control flow of logic
# function to get input from user
# function to calculate the total sales for the week
# function to display results to user


# create function to get input from user. Use weekdays as parameter
def daily_store_sales(weekdays):
    # create an empty list to store users input
    user_daily_sales = []
    # use a for loop to iterate through list of days of the week
    for day in weekdays:
        # ask user for input
        print('What were your sales for', day)
        # create a variable for the users input. store as float
        user_sales = float(input())
        # append users input to the list
        user_daily_sales.append(user_sales)
    # return the list
    return user_daily_sales


# create a function to calculate the total sales for the week. set user_daily sales as parameter
def weekly_store_sales(user_daily_sales):
    # create variable to store total sales. Set as zero originally
    total_sales = 0
    # use for loop to calculate the total sales based on the users input. use range function, and set length to number of days using list stored in user_daily_sales
    for daily_sales in range(len(user_daily_sales)):
        total_sales = total_sales + user_daily_sales[daily_sales]
    # return total sales
    return total_sales


# create function to display results.
def display_results(total_sales):
    # print the total sales for the week. format in $
    print('Total sales for the week were $', format(total_sales, '.2f'))


# create a main function to control flow of logic
def main():
    # store days of the week in a list
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    user_daily_sales = daily_store_sales(weekdays)
    total_sales = weekly_store_sales(user_daily_sales)
    display_results(total_sales)


# call the main function
main()
