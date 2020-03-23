# Joshua Torain CIS 115 FON04
# Write a program that writes a series of random numbers to a file. Each random number should be in the range of 1 through 500. The application should let the user specify how many random numbers the file will hold
# Make a main function to control flow of logic
# Import random to get random numbers
# make a function to get input from user for how many numbers the file will hold
# make a function to process the data being written to the file
# use for loop to pick numbers from range

# import random
import random


# function to get random numbers between 1 and 500
def get_random_numbers():
    # use randint function to generate random numbers between 1 and 500. store in variable
    random_numbers = random.randint(1, 500)
    # return the variable
    return random_numbers


# function to get input from user, return variable
def get_user_numbers():
    # get user input, store in variable
    user_numbers = int(input('How many numbers would you like in your file? '))
    # return the variable
    return user_numbers


# Main function to control flow of logic
def main():
    # open file for writing numbers, set to write
    numbers_file = open('random_numbers.txt', 'w')
    user_numbers = get_user_numbers()
    # use for loop to pick numbers in a range
    for numbers in range(1, user_numbers + 1):
        random_numbers = get_random_numbers()
        numbers_file.write(str(random_numbers) + '\n')
    # close the file
    numbers_file.close()


# call the main function
main()
