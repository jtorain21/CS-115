# Joshua Torain CIS 115 FON04
# write main function to control logic
# write functions to get the users name, age, and # of traffic violations
# write functions to determine risk code and risk type based on users input
# write a function to determine the insurance price based on user input
# write a function to display the results
# call the main function


# write main function to control logic
def main():
    name = customer_name()
    age = customer_age()
    traffic_violations = customer_traffic_violations()
    risk_code = customer_risk_code(traffic_violations)
    risk_type = customer_risk_type(risk_code)
    price = insurance_price(age, traffic_violations)
    display_results(name, risk_type, price)


# function to get users name
def customer_name():
    # store users input in variable called name
    name = input('What is your name? ')
    # return the variable, and capitalize it using capitalize() function
    return name.capitalize()


# function to get users age
def customer_age():
    # store users input as an integer in variable called age
    age = int(input('How old are you? '))
    # use a while loop to set age restrictions. use range() function, must be between 16 and 105
    while age not in range(16, 106):
        # if user enters invalid input print error message
        print('Drivers must be between 16 and 105 years of age!')
        # ask user to reenter age
        age = int(input('How old are you? '))
    # return the variable
    return age


# function to get number of traffic violations
def customer_traffic_violations():
    # store users input as an integer in variable called traffic_violations
    traffic_violations = int(input('How many traffic violations have you received? '))
    # use a while loop to set restrictions. must be zero or higher
    while traffic_violations < 0:
        # print error message is user gives invalid input
        print('Violations may not be less than 0!')
        # ask user to reenter data
        traffic_violations = int(input('How many traffic violations have you received? '))
    # return the variable
    return traffic_violations


# function to calculate the users risk code. use traffic_violations as parameter
def customer_risk_code(traffic_violations):
    # use if/elif statement to determine risk code based on number of traffic violations
    if traffic_violations == 0:
        risk_code = 4
    elif traffic_violations == 1:
        risk_code = 3
    elif traffic_violations == 2:
        risk_code = 2
    elif traffic_violations == 3:
        risk_code = 2
    else:
        risk_code = 1
    # return the variable
    return risk_code


# function to determine the users risk type, use risk_code as parameter
def customer_risk_type(risk_code):
    # use if/elif statement to determine risk type based on risk code
    if risk_code == 4:
        risk_type = 'no risk'
    elif risk_code == 3:
        risk_type = 'low risk'
    elif risk_code == 2:
        risk_type = 'moderate risk'
    else:
        risk_type = 'high risk'
    # return the variable
    return risk_type


# function to determine the users insurance price, age and traffic_violations are the parameters
def insurance_price(age, traffic_violations):
    # use if/elif statements to determine the price based on the users age and number of violations
    if age < 25 and traffic_violations > 3:
        price = '$480.00'
    elif age < 25 and traffic_violations == 3:
        price = '$450.00'
    elif age < 25 and traffic_violations == 2:
        price = '$405.00'
    elif age < 25 and traffic_violations == 1:
        price = '$380.00'
    elif age < 25 and traffic_violations == 0:
        price = '$325.00'
    elif age > 24 and traffic_violations > 3:
        price = '$410.00'
    elif age > 24 and traffic_violations == 3:
        price = '$390.00'
    elif age > 24 and traffic_violations == 2:
        price = '$365.00'
    elif age > 24 and traffic_violations == 1:
        price = '$315.00'
    else:
        price = '$275.00'
    # return the variable
    return price


# function to display the results to the user. Name, risk_type, and price are parameters
def display_results(name, risk_type, price):
    print(name, 'as a', risk_type, 'driver, your insurance will cost', price)


# use while loop to allow user to make multiple quotes
while True:
    # if user enters one, call the main function to run program
    if input('Would you like to make a quote? If yes, press 1 ') == '1':
        main()
    # if user enters anything other than one, use break to stop loop and end program.
    else:
        break
