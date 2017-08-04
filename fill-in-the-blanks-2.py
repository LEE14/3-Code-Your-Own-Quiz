# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/

allowed_choices = ['easy', '1', 'medium', '2', 'hard', '3']

current_phrase = []

data = {
    'easy': {
        'phrase': "Steven Paul ___1___ was an American entrepreneur, businessman, inventor, and industrial designer. He was the chairman, and the chief executive officer (CEO), and a co-founder of ___2___ Inc.; CEO and majority shareholder of ___3___; a member of The Walt Disney Company's board of directors following its acquisition of ___3___; and founder, chairman, and CEO of NeXT. ___1___ and Steve ___4___ are widely recognized as pioneers of the microcomputer revolution of the 1970s and 1980s.",
        'answers': ['Jobs', 'Apple', 'Pixar', 'Wozniak']
    },
    'medium': {
        'phrase': "William Henry ___1___ III is a co-founder of ___2___ and is an American business magnate, investor, author and philanthropist. In 1975, ___1___ and Paul Allen launched ___2___, which became the world's largest PC ___3___ company. During his career at ___2___, ___1___ held the positions of chairman, CEO and chief ___3___ architect, while also being the largest individual ___4___ until May 2014. In June 2006, ___1___ announced that he would be transitioning from full-time work at ___2___ to part-time work and full-time work at the Bill & Melinda ___1___ Foundation. He stepped down as chairman of ___2___ in February 2014 and assumed a new post as technology adviser to support the newly appointed CEO ___5___ Nadella.",
        'answers': ['Gates', 'Microsoft', 'software', 'shareholder', 'Satya']
    },
    'hard': {
        'phrase': "Sergey Mikhaylovich ___1___ is a Russian-born American computer scientist, internet entrepreneur, and philanthropist. Together with Larry Page, he co-founded ___2___. ___1___ is the President of ___2___'s parent company ___3___ Inc. ___1___ immigrated to the United States with his family from the Soviet Union at the age of 6. He earned his bachelor's degree at the University of Maryland, following in his father's and grandfather's footsteps by studying mathematics, as well as computer science. After graduation, he enrolled in ___4___ University to acquire a PhD in computer science. There he met Page, with whom he later became friends. They crammed their dormitory room with inexpensive computers and applied ___1___'s data mining system to build a web search engine. The program became popular at ___4___, and they suspended their PhD studies to start up ___2___ in a rented garage.",
        'answers': ['Brin', 'Google', 'Alphabet', 'Stanford']
    }
}

def play_game():
    """
    Behavior: Verify that the difficulty level entered by a user is valid
    Input: None
    Output: The difficulty level
    """
    while True:
        print 'Please select a game difficulty by typing it in!'
        print 'Possible choices include easy, medium, and hard.'
        user_choice = raw_input()
        if user_choice in allowed_choices:
            break
        else:
            print "That's not an option!"
            print
    if user_choice == allowed_choices[0] or user_choice == allowed_choices[1]:
        level = 'easy'
    if user_choice == allowed_choices[2] or user_choice == allowed_choices[3]:
        level = 'medium'
    if user_choice == allowed_choices[4] or user_choice == allowed_choices[5]:
        level = 'hard'
    current_phrase.append(data[level]['phrase'])
    print "You've chosen " + level + '!'
    print
    print 'You will get 5 guesses per problem'
    return level

def play_levels(level, current_question):
    """
    Behavior: Print the current question and check if the answer entered by a user is correct or wrong
    Input: the difficulty level and the current question number
    Output: True (if the answer is correct) or False (if the answer is wrong)
    """
    print
    print 'The current paragraph reads as such:'
    print current_phrase[0]
    print
    user_answer = raw_input('What should be substituted in for ' + '___' + str(current_question) + '___' + '? ').lower()
    print
    if user_answer == data[level]['answers'][current_question - 1].lower():
        return True
    else:
        return False

def correct_answer(level, current_question, max_attempts):
    """
    Behavior: Replace blanks in the current question with the correct answer and determine whether all questions are answered
    Input: the difficulty level, the current question number and mamxium permitted attempts
    Output: a number to update the current number of attempts, either 0 (if there are remaining questions, reset the current attempt) or maximum permitted attempts (if all questions are answered, break the while loop)
    """
    print 'Correct!'
    replaced = []
    temporary_text = current_phrase[0].split()
    for word in temporary_text:
        if '___' + str(current_question) + '___' in word:
            word = word.replace('___' + str(current_question) + '___', data[level]['answers'][current_question - 1])
            replaced.append(word)
        else:
            replaced.append(word)
    current_phrase[0] = " ".join(replaced)
    if current_question < len(data[level]['answers']):
        return 0
    else:
        print
        print current_phrase[0]
        print
        print 'You won!'
        return max_attempts

def wrong_answer(level, current_question, current_attempt, max_attempts):
    """
    Behavior: Print remaining attempts or the game over message
    Input: the difficulty level, the current question number, the current number of attempts and mamxium permitted attempts
    Output: a number to increase the current number of attempts by 1 (untimately beyond maximum permitted attempts to break the while loop)
    """
    if current_attempt < max_attempts - 1:
        print "That isn't the correct answer! Let's try again; you have " + str(max_attempts - current_attempt) + " trys left!"
    if current_attempt == max_attempts - 1:
        print "That isn't the correct answer! You have only 1 try left! Make it count!"
    if current_attempt == max_attempts:
        print "You've failed too many straight guesses! Game over!"
    return current_attempt + 1

def main():
    level = play_game()
    current_question = 1
    current_attempt = 1
    max_attempts = 5
    while current_attempt <= max_attempts:
        if play_levels(level, current_question):
            current_attempt = correct_answer(level, current_question, max_attempts) + 1
            current_question = current_question + 1
        else:
            current_attempt = wrong_answer(level, current_question, current_attempt, max_attempts)

# run main
main()
