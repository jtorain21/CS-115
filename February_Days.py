# Joshua Torain 1/20/2019 CIS-115 FON04

# First ask the user to enter a year. Year must be an integer < 0
# Figure out if number is divisible by 100. If yes, figure out if it is divisible by 400. If both are true, then display that it is a leap year to the user.  If is isn't divisible by 400 then display that it is not a leap year.
# If user inputted number is not divisible by 100, the figure out if it is divisible by 4.  If yes, then display that it is a leap year.  If not, then display that it is not a leap year
# If it is determined that it is a leap year display Februrary has 29 days.  If not, display February has 28 days.

# Ask user to input a year
year = int(input('Enter a year:'))

# Determine if it is a leap year. Use modulo to get remainder.  It must be zero or year is not is not divisible by the number. If none are true then it is not a leap year.
if year % 100 == 0 and year % 400 == 0:
    print('In', year, 'February has 29 days')
elif year % 100 != 0 and year % 4 == 0:
    print('In', year, 'February has 29 days')
else:
    print('In', year, 'February has 28 days')
