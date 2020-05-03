# Joshua Torain CIS 115 FON04
# write a main function to control the flow of logic
# function to get input from user
# function to convert date format
# function to display results


# write a function to get the date from user
def get_user_date():
    # use input function to prompt user to enter date in specified format. store in variable
    user_date = input('Enter a date in the format mm/dd/yyyy: ')
    # return the variable
    return user_date


# write a function to convert date format
def convert_date_format(user_date):
    # use split method to split date by "/" to separate month, day and year. store as variable for list
    user_date_values = user_date.split('/')
    # create variables for each individual value of the date
    user_date_month = user_date_values[0]
    user_date_day = user_date_values[1]
    user_date_year = user_date_values[2]
    # return the variables
    return user_date_month, user_date_day, user_date_year


# write function to format month to correct form
def change_date(user_date_month):
    # create a list for month names
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    index = (user_date_month) - 1
    month = months[index]
    return month


# write function to display date
def display_date(month, user_date_day, user_date_year):
    print('The date is', month, user_date_day, ',', user_date_year)


# write main function
def main():
    user_date = get_user_date()
    user_date_month = convert_date_format(user_date)
    user_date_day = convert_date_format(user_date)
    user_date_year = convert_date_format(user_date)
    month = change_date(user_date_month)
    display_date(month, user_date_day, user_date_year)


# call the main function
main()
