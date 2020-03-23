# Joshua Torain CIS - 115 FON04
# create a main function to control logic
# open the file, set mode to read, store in variable
# use for loop to read all lines from the file
# create variable for the sum of all numbers, in for loop add total from previous line to next to add all numbers


# create main function to control logic
def main():
    # open file, set mode to read, store in variable
    numbers = open('numbers.txt', 'r')
    # create variable for sum of all numbers. set initally to zero
    numbers_sum = 0
    # use for loop to read all lines from file
    for line in numbers:
        # use int() to turn numbers from string to integer so they can be added
        numbers_sum = numbers_sum + int(line)
    # print the sum of all numbers
    print('The sum of all the numbers in this file is', numbers_sum)

    # close the file
    numbers.close()


# call the main function
main()
