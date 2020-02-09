# Joshua Torain CIS - 115 FON04

# write main function to control logic
# write function to ask user for the value of their land
# write function to calculate the assessment value of the land, which is 60% of actual value
# write function to calculate the property tax, which is $0.72 for every $100 of the assessment value
# wrtie function to display the assessment value and property tax


# write main function
def main():
    user_property_value = property_value()
    assessment_value = calculate_assessment_value(user_property_value)
    property_tax = calculate_property_tax(assessment_value)
    display_values(user_property_value, assessment_value, property_tax)


# ask user for value of their property. Store as a float
def property_value():
    # create variable to store users input
    user_property_value = float(input("What is the value of your property? "))
    # return variable
    return user_property_value


# write function to calculate assessment value. Use property value from user as parameter
def calculate_assessment_value(user_property_value):
    # create variable to store calculation. assessment value is 60% of property value
    assessment_value = user_property_value * .60
    # return variable
    return assessment_value


# write function to calculate the property tax. Use assessment value as parameter
def calculate_property_tax(assessment_value):
    # create variable to store calculation. Property tax is $0.72 for every $100
    property_tax = (assessment_value / 100) * 0.72
    # return variable
    return property_tax


# write function to display assessment value and property tax. Use previous variables as parameters. Format in dollars.
def display_values(user_property_value, assessment_value, property_tax):
    print("The Assessment Value is $ ", format(assessment_value, ',.2f'))
    print("The Property Tax is $ ", format(property_tax, ',.2f'))


# call main function
main()
