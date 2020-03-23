# Joshua Torain CIS 115 FON04
# Write a program that reads the random numbers from the file, displays the numbers, total sum, and number of random numbers
# main function to control flow of lodgic
# functions to do processes


# main function to control flow of logic
def main():
    # open the file and read it
    number_file = open('random_numbers.txt', 'r')
    display_numbers(number_file)
    total_numbers(number_file)
    total_of_numbers(number_file)
    number_file.close()


# function to display numbers
def display_numbers(number_file):
    # read file using .read() and store it in variable
    contents = number_file.read()
    # display the files contents
    print(contents)


# function to get sum of the numbers
def total_of_numbers(number_file):
    # create variable for sum of all numbers. set initally to zero
    numbers_sum = 0
    # use for loop to read all numbers from file
    for numbers in number_file:
        # use int() to turn numbers from string to integer so they can be added
        numbers_sum = numbers_sum + int(numbers)
    # disply the sum of the numbers
    print('The sum of the numbers in this file is', str(numbers_sum))


# function to get number of numbers in the file
def total_numbers(number_file):
    # use readline function to read the first line in the file. store it in variable
    numbers = number_file.readlines()
    # create variable to keep track of number of lines in file. store it as zero to begin
    number_of_numbers = 0
    # use while loop to read each line until it gets to an empty string, signifying the end of the file
    while numbers != "":
        # add 1 to variable number of lines, to have loop read next line in file
        number_of_numbers = number_of_numbers + 1
        # use readline function again to read next line
        numbers = number_file.readlines()
    # display the total numbers in file
    print('There are', str(numbers), 'in this file.')


# call the main function
main()
