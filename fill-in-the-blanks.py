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

difficulty = ['easy', 'medium', 'hard']

text_easy = '''Steven Paul ___1___ was an American entrepreneur, businessman, inventor, and industrial designer. He was the chairman, and the chief executive officer (CEO), and a co-founder of ___2___ Inc.; CEO and majority shareholder of ___3___; a member of The Walt Disney Company's board of directors following its acquisition of ___3___; and founder, chairman, and CEO of NeXT. ___1___ and Steve ___4___ are widely recognized as pioneers of the microcomputer revolution of the 1970s and 1980s.'''

answer_easy = ['Jobs', 'Apple', 'Pixar', 'Wozniak']

text_medium = '''William Henry ___1___ III is a co-founder of ___2___ and is an American business magnate, investor, author and philanthropist. In 1975, ___1___ and Paul Allen launched ___2___, which became the world's largest PC ___3___ company. During his career at ___2___, ___1___ held the positions of chairman, CEO and chief ___3___ architect, while also being the largest individual ___4___ until May 2014. In June 2006, ___1___ announced that he would be transitioning from full-time work at ___2___ to part-time work and full-time work at the Bill & Melinda ___1___ Foundation. He stepped down as chairman of ___2___ in February 2014 and assumed a new post as technology adviser to support the newly appointed CEO ___5___ Nadella.'''

answer_medium = ['Gates', 'Microsoft', 'software', 'shareholder', 'Satya']

text_hard = '''Sergey Mikhaylovich ___1___ is a Russian-born American computer scientist, internet entrepreneur, and philanthropist. Together with Larry Page, he co-founded ___2___. ___1___ is the President of ___2___'s parent company ___3___ Inc. ___1___ immigrated to the United States with his family from the Soviet Union at the age of 6. He earned his bachelor's degree at the University of Maryland, following in his father's and grandfather's footsteps by studying mathematics, as well as computer science. After graduation, he enrolled in ___4___ University to acquire a PhD in computer science. There he met Page, with whom he later became friends. They crammed their dormitory room with inexpensive computers and applied ___1___'s data mining system to build a web search engine. The program became popular at ___4___, and they suspended their PhD studies to start up ___2___ in a rented garage.'''

answer_hard = ['Brin', 'Google', 'Alphabet', 'Stanford']

# 'check_difficulty' takes user's choice of difficulty as input and returns the corresponding level of difficulty. If user's choice does not match 'easy', 'medium' or 'hard', it returns None to prompt the user to re-enter a correct choice.
def check_difficulty(choice):
    if choice == '1' or choice == 'easy':
        return 'easy'
    if choice == '2' or choice == 'medium':
        return 'medium'
    if choice == '3' or choice == 'hard':
        return 'hard'
    else:
        return None

# 'select_difficulty' takes user's choice of difficulty as input and returns the text and answer of corresponding difficulty. User's choice should be checked by the 'check_difficulty' function before it is used as input for this fuction.
def select_difficulty(choice):
    if choice == 'easy':
        return text_easy, answer_easy
    if choice == 'medium':
        return text_medium, answer_medium
    if choice == 'hard':
        return text_hard, answer_hard

# 'create_blank' takes a question number as input and returns the blank with the question number.
def create_blank(question):
    return '___' + str(question) + '___'

# 'update_text' takes a text and a question number as input and returns the revised text which replaces blanks for the question with an answer.
def update_text(text, question):
    place_holder = create_blank(question)
    replaced = []
    text = text.split()
    for word in text:
        if place_holder in word:
            word = word.replace(place_holder, answer[question - 1])
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced

# 'play_game' takes a question number and the number of allowed attempts as input and asks a user to enter his / her guess for the question. If the user enters a correct guess within allowed attempts, it moves on to the next question. If the user gets all the guesses right, it will return 'correct'. However, if the user enters a wrong guess, it reminds the user of remaining attempts and prompts him / her to try again. If the user exhausts all available attempts, it will return 'wrong'. The returned value, 'correct' or 'wrong', is used to determine the final text to be printed before the program closes.
def play_game(question, attempt):
    place_holder = create_blank(question)
    while attempt > 0:
        print
        print 'The current paragraph reads as such:'
        print text
        print
        user_input = raw_input('What should be substituted in for ' + place_holder + '? ')
        print
        if user_input == answer[question - 1]:
            print 'Correct!'
            return 'correct'
        else:
            attempt = attempt - 1
            if attempt > 1:
                print "That isn't the correct answer! Let's try again; you have " + str(attempt) + " trys left!"
            if attempt == 1:
                print "That isn't the correct answer! You have only " + str(attempt) + " try left! Make it count!"
    return 'wrong'

# This section asks a user to enter his / her choice of difficulty, checks the choice against acceptable values and, if the choice is not valid, requests the user to enter an appropriate value again.
choice = ''
while check_difficulty(choice) not in difficulty:
    print 'Please select a game difficulty by typing it in!'
    print 'Possible choices include easy, medium, and hard.'
    choice = raw_input()
    if check_difficulty(choice) not in difficulty:
        print "That's not an option!"
        print
    else:
        choice = check_difficulty(choice)

# This section prints difficulty entered by a user and the number of available attempts to make guesses.
text, answer = select_difficulty(choice)
print
print "You've chosen " + choice + '!'
print
question = 1
attempt = 5
print 'You will get ' + str(attempt) + ' guesses per problem'

# This section goes from the first question to the last one and moves on the next section if the user exhausts all available attempts or gets all gueses right. During the process, it updates the text by replacing blanks for each question with answers correctly entered by a user.
while question < len(answer) + 1:
    result = play_game(question, attempt)
    if result == 'wrong':
        break
    text = update_text(text, question)
    question = question + 1
    attempt = 5

# This section prints two different final texts depending on the result of the previous section, or the value reterned by the 'play_game' function.
if result == 'correct':
    print
    print text
    print
    print 'You won!'
else:
    print "You've failed too many straight guesses! Game over!"
