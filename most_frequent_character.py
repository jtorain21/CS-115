# Joshua Torain CIS 115 FON04
# create main function to control flow of logic
# create function to get input from user
# create function to find which character appears most frequently
# create function that displays results


# create function to get input from user
def get_user_input():
    # use input() to prompt user. store their input into variable
    user_input = input('Please enter your characters: ')
    # return the variabel
    return user_input


# create function to find most frequent character
def get_most_frequent(user_input):
    # create empty list to store characters
    characters = []
    # create empty list to store count of each character
    count_of_characters = []
    # use for loop to iterate though users characters
    for ch in user_input:
        # if a character is not already in list append to the list and count
        if ch not in characters:
            characters.append(ch)
            count_of_characters.append(1)
        # if character is in list, add 1 to its count
        else:
            position = characters.index(ch)
            count_of_characters[position] = count_of_characters[position] + 1
            # use max() to find index with highest value in list
            most_frequent = characters[count_of_characters.index(max(count_of_characters))]
    # return the variable
    return most_frequent


# create a function to display results to user
def display_results(most_frequent):
    print('The most frequent character is', most_frequent)


# create a main function
def main():
    user_input = get_user_input()
    most_frequent = get_most_frequent(user_input)
    display_results(most_frequent)


# call the main function
main()
