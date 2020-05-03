# Joshua Torain CIS 115 FON04
# create main function to control flow of logic
# create function to open file and count number of upper, lower, digits, and whitespace
# create function to display the results


# create a function to open the file and store the contents into a variable
def read_file():
    # open file and set to read
    text_file = open('text.txt', 'r')
    # read file and store in variable
    contents = text_file.read()
    # return the variable
    return contents


# create function to count number of upper, lower, digits, and whitespace
def count_characters(contents):
    # create variables for each and set initally to zero
    uppercase = 0
    lowercase = 0
    digits = 0
    whitespace = 0
    # use for loop to iterate through text to count number of each type
    for characters in contents:
        if characters.isupper():
            uppercase += 1
        elif characters.islower():
            lowercase += 1
        elif characters.isdigit():
            digits += 1
        elif characters.isspace():
            whitespace += 1
    # return each of the variables
    return uppercase, lowercase, digits, whitespace


# create function to display the number of each type of character
def display_results(uppercase, lowercase, digits, whitespace):
    print('Uppercase Letters:', uppercase)
    print('Lowercase Letters:', lowercase)
    print('Digits:', digits)
    print('Whitespace:', whitespace)


# create a main function to control flow of logic
def main():
    contents = read_file()
    uppercase, lowercase, digits, whitespace = count_characters(contents)
    display_results(uppercase, lowercase, digits, whitespace)


# call the main function
main()
