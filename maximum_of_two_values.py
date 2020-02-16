# Joshua Torain CIS-115 FON04
# write a main function to control logic
# write functions to get user input
# write function named max that accepts two integer values as arguments and returns the value that is the greater of the two.


# write a function to get user numbers
def get_numbers():
    # create variables to store the users input numbers. use int() function
    first_number = int(input('What is your first number? '))
    second_number = int(input('What is your second number? '))
    # return the variables
    return first_number, second_number


# create a function named max to get max value. Use if/else statement to return the higher value
def max(first_number, second_number):
    if first_number > second_number:
        return first_number
    else:
        return second_number


# create main function to control flow of logic
def main():
    first_number, second_number = get_numbers()
    # print out the returned value from max() function.
    print('The maximum value is ', max(first_number, second_number))
    return


# call main function
main()
