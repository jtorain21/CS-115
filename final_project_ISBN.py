# Joshua Torain CIS 115 FON04
# main function to control flow of logic
# function to get input from user (10-digit ISBN or 13-digit ISBN)
# function to verify check digit of ISBN-10
# function to verify check digit of ISBN-13
# function to convert ISBN-10 to ISBN-13
# function to convert ISBN-10 to ISBN-13
# function to display menu

# import sys to exit program
import sys


# function to display menu
def display_menu():
    user_option = input("""    Please choose an option:

    1. Verify the check digit of an ISBN-10
    2. Verify the check digit of an ISBN-13
    3. Convert an ISBN-10 to an ISBN-13
    4. Convert an ISBN-13 to an ISBN-10
    5. Exit
    """)
    if user_option == "1":
        print("Verifying the check digit!")
    elif user_option == "2":
        print("Verifying the check digit!")
    elif user_option == "3":
        print("Converting the ISBN-10 to an ISBN-13!")
    elif user_option == "4":
        print("Converting the ISBN-13 to an ISBN-10!")
    elif user_option == "5":
        sys.exit()
    elif user_option != "":
        print("Please choose a valid option")
    return user_option


# write function to get user ISBN-10
def get_isbn_10():
    user_isbn_10 = input("Please enter your ISBN-10 with no dashes: ")
    # use while loop to restrict user to 10 digits
    while len(user_isbn_10) != 10 or (not user_isbn_10.isdigit()):
        print("This is not a valid input!")
        user_isbn_10 = input("Please enter your ISBN-10 with no dashes: ")
    return user_isbn_10


# write function to get user ISBN-13
def get_isbn_13():
    user_isbn_13 = input("Please enter your ISBN-13 with no dashes: ")
    # use while loop to restrict user to 13 digits
    while len(user_isbn_13) != 13 or (not user_isbn_13.isdigit()):
        print("This is not a valid input!")
        user_isbn_13 = input("Please enter your ISBN-13 with no dashes: ")
    return user_isbn_13


# write function to verify check digit of ISBN-10
def verify_isbn_10(user_isbn_10):
    # find sum of digits of user input multiplied by weights
    sum_isbn_10 = int(user_isbn_10[0]) * 10 + int(user_isbn_10[1]) * 9 + int(user_isbn_10[2]) * 8 + int(user_isbn_10[3]) * 7 + int(user_isbn_10[4]) * 6 + int(user_isbn_10[5]) * 5 + int(user_isbn_10[6]) * 4 + int(user_isbn_10[7]) * 3 + int(user_isbn_10[8]) * 2 + int(user_isbn_10[9]) * 1
    # find if sum is divisible by 11 using modulo
    if sum_isbn_10 % 11 == 0:
        print("The check digit " + (user_isbn_10[9]) + " is valid.")
        print(user_isbn_10 + " is a valid ISBN.")
    else:
        print("The check digit " + (user_isbn_10[9]) + " is invalid.")
        print(user_isbn_10 + " is not a valid ISBN.")


# write function to verify ISBN-13 check digit
def verify_isbn_13(user_isbn_13):
    # find sum of digits of user input multiplied by weights
    sum_isbn_13 = int(user_isbn_13[0]) * 1 + int(user_isbn_13[1]) * 3 + int(user_isbn_13[2]) * 1 + int(user_isbn_13[3]) * 3 + int(user_isbn_13[4]) * 1 + int(user_isbn_13[5]) * 3 + int(user_isbn_13[6]) * 1 + int(user_isbn_13[7]) * 3 + int(user_isbn_13[8]) * 1 + int(user_isbn_13[9]) * 3 + int(user_isbn_13[10]) * 1 + int(user_isbn_13[11]) * 3 + int(user_isbn_13[12])
    # find if sum is divisible by 13 using modulo
    if sum_isbn_13 % 10 == 0:
        print("The check digit " + (user_isbn_13[12]) + " is valid.")
        print(user_isbn_13 + " is a valid ISBN.")
    else:
        print("The check digit " + (user_isbn_13[12]) + " is invalid.")
        print(user_isbn_13 + " is not a valid ISBN.")


# write function to convert ISBN-10 to ISBN-13
def convert_isbn_10(user_isbn_10):
    # remove check digit from user isbn and add 978
    user_isbn_13 = "978" + user_isbn_10[:-1]
    # convert new variable to string
    new_isbn_13 = str(user_isbn_13)
    check_digit = 0
    # use for loop to iterate through
    for i in range(len(new_isbn_13)):
        if i % 2 == 0:
            check_digit += int(new_isbn_13[i])
        else:
            check_digit += int(new_isbn_13[i]) * 3
    check_digit = check_digit % 10
    isbn_13 = str(user_isbn_13) + str(check_digit)
    print("The ISBN-13 is " + isbn_13)


# write function to convert ISBN-13 to ISBN-10
def convert_isbn_13(user_isbn_13):
    # remove 978 and check digit
    user_isbn_10 = user_isbn_13[3:-1]
    check_digit = 0
    new_isbn_10 = str(user_isbn_10)
    # use for loop
    for i in range(len(new_isbn_10)):
        if i % 2 == 0:
            check_digit += int(new_isbn_10[i])
        else:
            check_digit += int(new_isbn_10[i]) * 3
    check_digit = 10 - (check_digit % 10)
    isbn_10 = str(new_isbn_10) + str(check_digit)
    print("The ISBN-10 is " + isbn_10)


# write main function to control the flow of logic
def main():
    user_option = display_menu()
    if user_option == "1":
        user_isbn_10 = get_isbn_10()
        verify_isbn_10(user_isbn_10)
    elif user_option == "2":
        user_isbn_13 = get_isbn_13()
        verify_isbn_13(user_isbn_13)
    elif user_option == "3":
        user_isbn_10 = get_isbn_10()
        convert_isbn_10(user_isbn_10)
    elif user_option == "4":
        user_isbn_13 = get_isbn_13()
        convert_isbn_13(user_isbn_13)


# call the main function
main()
