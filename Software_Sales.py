# Joshua Torain 1/20/20 CIS-115 FON04

# First ask the user how many packages they ordered, and calculate total amount before discount
# Calculate the amount of discount they should recieve based on the input. Use elif statement
# Calculate the total amount after the discount
# Lastly show user how much of a discount they recieved and their final total cost

# Ask user how many packages they purchased. Store it as an integer, in a variable.
number_of_packages_ordered = int(input('How many packages did you purchase?'))

# Calculate total amount before discount
total_amount_before_discount = number_of_packages_ordered * 99
total_amount_before_discount_in_dollars = format(total_amount_before_discount, ',.2f')

# Calculate total amounts after discount
if number_of_packages_ordered > 9 and number_of_packages_ordered < 20:
    discount = total_amount_before_discount * 0.10
    total_amount_after_discount = total_amount_before_discount - discount
    total_amount_after_discount_in_dollars = format(total_amount_after_discount, ',.2f')
    discount_in_dollars = format(discount, ',.2f')
elif number_of_packages_ordered > 19 and number_of_packages_ordered < 50:
    discount = total_amount_before_discount * 0.20
    total_amount_after_discount = total_amount_before_discount - discount
    total_amount_after_discount_in_dollars = format(total_amount_after_discount, ',.2f')
    discount_in_dollars = format(discount, ',.2f')
elif number_of_packages_ordered > 49 and number_of_packages_ordered < 100:
    discount = total_amount_before_discount * 0.30
    total_amount_after_discount = total_amount_before_discount - discount
    total_amount_after_discount_in_dollars = format(total_amount_after_discount, ',.2f')
    discount_in_dollars = format(discount, ',.2f')
else:
    discount = total_amount_before_discount * 0.40
    total_amount_after_discount = total_amount_before_discount - discount
    total_amount_after_discount_in_dollars = format(total_amount_after_discount, ',.2f')
    discount_in_dollars = format(discount, ',.2f')
# Display the amount of discount they received and total price based on users input
if number_of_packages_ordered < 10:
    print('I\'m sorry you do not qualify for a discount.')
    print('Your total amount is $', total_amount_before_discount_in_dollars)
elif number_of_packages_ordered > 9 and number_of_packages_ordered < 20:
    print('Your price is discounted 10%')
    print('Your total after the discount is $', total_amount_after_discount_in_dollars)
    print('You saved $', discount_in_dollars)
elif number_of_packages_ordered > 19 and number_of_packages_ordered <50:
    print('Your price is discounted 20%')
    print('Your total after the discount is $', total_amount_after_discount_in_dollars)
    print('You saved $', discount_in_dollars)
elif number_of_packages_ordered > 49 and number_of_packages_ordered <100:
    print('Your price is discounted 30%')
    print('Your total after the discount is $', total_amount_after_discount_in_dollars)
    print('You saved $', discount_in_dollars)
else:
    print('Your price is discounted 40%')
    print('Your total after the discount is $', total_amount_after_discount_in_dollars)
    print('You saved $', discount_in_dollars)