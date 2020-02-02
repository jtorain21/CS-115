# Tuition is $8000, will increase 3% each year for the next 5 years
# Set variables, create a formula for new tuition each year
# Tuition for current year = 8000, year 1 = 8240, year 2 = 8487.20, year 3 = 8741.82, year 4 = 9004.07, year 5 = 9274.19

# Print table header
print('Year\t Projected Tuition')
print('--------------------------')
# print the current tuition which is $8000
print('Current', '\t', '$ 8000.00')
# set tuition variable as 8000
tuition = 8000
# set increasing percentage variable as 3% which is .03
tuition_increase_percentage = .03
# Use a for loop with the range function to iterate years 1 through 5
for year in range(1, 6):
    # create formula to figure out tuition for each year. need to add the increase to the previous years tuition and store it as tuition for the next iteration.
    tuition = tuition + (tuition_increase_percentage * tuition)
    # print the year and tuition for that year. Format in dollars (two decimal places), add $ sign
    print(year, '\t', '\t', '$', format(tuition, '.2f'))
