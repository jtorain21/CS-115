# Joshua Torain CIS 115 FON04
# Design a program that asks user to enter a series of 20 numbers. The program should store the numbers in a list then display the following data
# The lowest number in the list
# The highest number in the list
# The Total of the numbers in the list
# The average of the numbers in the list

# main function to control flow of logig
# function to get input from user
# functions to process calculations (lowest, highest, sum, and average)
# function to display results


# create function to get input from user. use amount_of_user_numbers as parameter
def get_user_input(amount_of_user_numbers):
    # create an empty list to store users numbers
    user_number_list = []
    # use for loop to ask user for 20 numbers. set range to user_numbers
    for user_input_number in range(amount_of_user_numbers):
        # use input function to ask user for numbers. convert to integer
        user_number = int(input('Enter a number '+ str(user_input_number + 1) + ': '))
        # append users numbers to list
        user_number_list.append(user_number)
    # return the users list
    return user_number_list


# create function to find lowest number. Use min function
def user_lowest_number(user_number_list):
    # use min function to find lowest number. store in variable
    lowest_number = min(user_number_list)
    # return the variable
    return lowest_number


# create function to find highest number. use max function
def user_highest_number(user_number_list):
    # use max function to find highest number. store in variable
    highest_number = max(user_number_list)
    # return the variable
    return highest_number


# create function to calculate total of numbers. use for loop
def calculate_sum_of_numbers(user_number_list):
    # create variable to store sum as loop iterates. set initally as 0
    number_total = 0
    # use for loop to find total of numbers. use range function with length of list
    for user_input_number in range(len(user_number_list)):
        number_total = number_total + user_number_list[user_input_number]
    # return the variable
    return number_total


# create function to calculate the avg. need two parameters list and the sum of numbers
def calculate_average_of_numbers(user_number_list, number_total):
    # find out how many numbers in list by using len function
    total_numbers = len(user_number_list)
    # calculate the avg by taking sum and dividing by total number of numbers. set as variable
    average_of_numbers = number_total / total_numbers
    # return the variable
    return average_of_numbers


# create function to display results
def display_results(user_number_list, lowest_number, highest_number, number_total, average_of_numbers):
    print('The lowest number is', lowest_number)
    print('The highest number is', highest_number)
    print('The total of all the number is', number_total)
    print('The average of the numbers is', average_of_numbers)


# create a main function to control flow of logig
def main():
    # create variable for amount of user numbers. must be 20
    amount_of_user_numbers = 20
    # create empty list to store user numbers
    user_number_list = []
    user_number_list = get_user_input(amount_of_user_numbers)
    lowest_number = user_lowest_number(user_number_list)
    highest_number = user_highest_number(user_number_list)
    number_total = calculate_sum_of_numbers(user_number_list)
    average_of_numbers = calculate_average_of_numbers(user_number_list, number_total)
    display_results(user_number_list, lowest_number, highest_number, number_total, average_of_numbers)


# call the main function
main()
