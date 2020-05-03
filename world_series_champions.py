# Joshua Torain CIS 115 FON04
# create main function to control flow of logic
# create function to open the file and read list of champions
# create function to get number of titles each champion has
# create function to get user input


# create function to open file and read list of champions
def list_of_championship_teams(file_name):
    # open the file, set mode to read, store as variable
    champions_file = open(file_name, 'r')
    # create an empty list to store champions
    list_of_champions = []
    # use readline() to read list of champions from file
    champions = champions_file.readline()
    # use while loop to iterate through file and read each line until it gets to and empty string
    while champions != '':
        # append each champion to the empty list
        list_of_champions.append(champions)
        # read the next line after appending until loop is done
        champions = champions_file.readline()
    # return the list
    return list_of_champions


# create function to get user input
def get_user_team():
    user_team = input('Which team would you like to search for? ')
    return user_team


# create a function to get number of titles for each team.
def list_of_titles(user_team, list_of_champions):
    # create variable to store number of titles. set initially to zero
    championships = 0
    # use for loop to iterate though index
    for index in range(len(list_of_champions)):
        if list_of_champions[index] == user_team:
            championships = championships + 1
    # return the variable
    return championships


# create function to display results to user
def display_results(user_team, championships):
    print(user_team, 'has won the World Series', championships, 'times!')


# create main function to control flow of logic
def main():
    file_name = 'WorldSeriesWinners.txt'
    list_of_champions = list_of_championship_teams(file_name)
    user_team = get_user_team()
    championships = list_of_titles(user_team, list_of_champions)
    display_results(user_team, championships)


# call the main function
main()
