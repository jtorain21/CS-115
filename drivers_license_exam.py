# Joshua Torain CIS 115 FON04
# create main function to control flow of logic
# create a function to get answers from users
# create a function to read users answers and store in another list
# create functions to determine number of correct answers, incorrect answers and whether or not student passed or failed.


# create function to get answers from user. store users answers in file
def get_user_answers(file_name, user_correct_answers):
    # open the file. set to write, store in variable
    user_answers_file = open(file_name, 'w')
    # create variable for number of question on exam. use len() function
    number_of_questions = len(user_correct_answers)
    # use for loop to prompt user for answers to questions. use range() function
    for current_user_question in range(number_of_questions):
        # use input() to prompt user. make users current question a string using str(). store as variable
        user_answer = input('Question' + str(current_user_question + 1) + ':')
        # write users answers to file
        user_answers_file.write(user_answer)
    # close the file
    user_answers_file.close()


# create function to read student's answers from text file and store answers in a list.
def read_user_answers(file_name):
    # create empty list to store answers
    user_answers = []
    # open file, set it to read mode. store it in variable
    user_answers_file = open(file_name, 'r')
    # use for loop to read through list of user answers
    for user_answer in user_answers_file:
        # use append() to append answers to list
        user_answers.append(user_answer)
    # return the variable containing list
    return user_answers


# create function to determine number of correct answers
def number_of_correct_answers(exam_correct_answers, user_correct_answers):
    # create variable to store number of correct answers. initially set to zero
    correct_answers = 0
    # create variable for number of question on exam. use len() function
    number_of_questions = len(exam_correct_answers)
    # use for loop to iterate through users answers and exam answers to compare them and determine how many are correct
    for current_user_question in range(number_of_questions):
        # use if statement to add correct answer to count.
        if user_correct_answers[current_user_question] == exam_correct_answers[current_user_question]:
            correct_answers = correct_answers + 1
    # return the numbers of correct answers.
    return correct_answers


# create function to determine number of incorrect answers
def number_of_incorrect_answers(number_of_correct_answers, number_of_questions):
    # create variable to store number of incorrect answers. subract number of correct answers from total number of questions to get number of incorrect answers
    incorrect_answers = number_of_questions - number_of_correct_answers
    # return the variable
    return incorrect_answers


# create function to show incorrect answers.
def show_incorrect_answers(exam_correct_answers, user_correct_answers):
    # create empty list to store incorrect answers
    incorrect_answers_list = []
    # create variable to store number of questions. 
    number_of_questions = len(exam_correct_answers)
    # use for loop to iterate through questions to compare student answer to correct answer
    for current_user_question in range(number_of_questions):
        # use if statement to 
        if user_correct_answers[current_user_question] != exam_correct_answers[current_user_question]:
            # append to list
            incorrect_answers_list.append(current_user_question + 1)
        # return list
        return incorrect_answers_list


# create function to determine if user passed
def user_pass_exam(passed_number, user_correct_answers):
    # use if/else statement to determine if user passed
    if len(user_correct_answers) >= passed_number:
        return True
    else:
        return False


# create function to display results
def display_results(number_of_correct_answers, number_of_incorrect_answers, incorrect_questions):
    # print number of correct answers
    print('You answered' + str(number_of_correct_answers) + 'correctly!')
    # print number of incorrect answers
    print('You answered' + str(number_of_incorrect_answers) + 'incorrectly!')


# create main function to control flow of logic
def main():
    exam_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
    file_name = 'answers.txt'
    number_of_questions = len(exam_answers)
    get_user_answers(file_name, user_correct_answers)
    user_answers = read_user_answers(file_name)
    correct_answers = number_of_correct_answers(exam_correct_answers, user_correct_answers)
    incorrect_answers = number_of_incorrect_answers(number_of_correct_answers, number_of_questions)
    incorrect_answers_list = show_incorrect_answers(exam_correct_answers, user_correct_answers)
    user_pass_exam(passed_number, user_correct_answers)
    display_results(number_of_correct_answers, number_of_incorrect_answers, incorrect_questions)


# call the main function
main()
