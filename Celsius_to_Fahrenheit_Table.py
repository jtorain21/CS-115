# Set Variables - celsius = 0
# Set up the conversion of Celsius to Fahrenheit using the formula
# Set the range of temperatures from 0 to 20
# Use a while loop to iterate over each value 0 through 20.

# Formula --> F = (9/5) * C + 32

# print table heading
print('Celsius\tFahrenheit')
print('-------------------')

# create celsius variable. Make it zero since that's our starting temperature
celsius = 0
# Create a while loop to iterate over each value from 0 through 20. Print out the values
# Set range of temperatures to be from 0 to 20 Celsius
while 0 <= celsius <= 20:
    # enter conversion formula.  changed (9/5) to 1.8 for simplicity
    fahrenheit = (celsius * 1.8) + 32
    # print out temperatures. Format fahrenheit so that it only displays one number after decimal
    print(celsius, '\t', format(fahrenheit, '.1f'))
    # set celsius variable to count by one, to repeat loop until 20
    celsius = celsius + 1
# While loop should terminate once it reaches 20 and it is "no longer true"
