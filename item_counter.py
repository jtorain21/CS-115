# Joshua Torain CIS - 115 FON04
# create a main function to control logic
# open the file and set mode to read, store in variable
# use a while loop to read each line until it gets to an empty string
# store the number of lines in a variable, then print out the variable
# call the main function


# create  a main function to control logic
def main():
    # open file, set mode to read, store in variable
    names = open('names.txt', 'r')
    # use readline function to read the first line in the file. store it in variable
    line = names.readline()
    # create variable to keep track of number of lines in file. store it as zero to begin
    number_of_lines = 0
    # use while loop to read each line until it gets to an empty string, signifying the end of the file
    while line != "":
        # add 1 to variable number of lines, to have loop read next line in file
        number_of_lines = number_of_lines + 1
        # use readline function again to read next line
        line = names.readline()
    # print the variable "number_of_lines" after while loop ends
    print('This file contains', number_of_lines, 'lines.')
    # close the file
    names.close()


# call main function
main()
