# Joshua Torain CIS 115 FON04
# write a main function to control flow of logic
# function to get input from user
# function to get sum of digits
# function to display the results


# write input to get input from user
def input_from_user():
    # use input function to prompt user to enter numbers
    user_number = input('Enter a series of single digits numbers with no separation: ')
    # return the variable
    return user_number


# write function to find sum of digits in user's number
def sum_of_user_number(user_number):
    # create variable to store the sume of digits in user's number. set to 0 initially
    sum_of_digits = 0
    # use for loop to iterate through index
    for index in user_number:
        digit = int(index)
        sum_of_digits = sum_of_digits + digit
    # return the variable
    return sum_of_digits


# write a function to display the results
def display_results(user_number, sum_of_digits):
    print('The sum of the digits in', user_number, 'is', sum_of_digits)


# write main function to control flow of logic
def main():
    user_number = input_from_user()
    sum_of_digits = sum_of_user_number(user_number)
    display_results(user_number, sum_of_digits)


# call the main function
main()
