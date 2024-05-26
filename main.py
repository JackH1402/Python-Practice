play = "yes"

QUESTION_FORMAT = "{}\nA.{} B.{} C.{} D.{}"
GOOD_COMMENTS = ["Good job!", "Keep it up!", "Your on a roll!"]
BAD_COMMENTS = ["Unlucky", "Keep trying", "You need some help"]

QUESTIONS = ["What is the smallest country by land mass?",
              "What country has the highest population?",
                "What country has the lowest sea level?",]

OPTIONS = [["San Marino", "Tonga", "Russia", "Vatican City"],
            ["Sri Lanka", "India", "China", "France"],
             ["Qatar", "Denmark", "New Zealand", "Maldives"]]
SHORT_OPTIONS = ["a", "b", "c", "d"]
ANSWERS = [3,1,3]

import random
score = 0

# Ask the user there name
name = input("What's your name?")
# Greet the user and introduce the quiz
print("Welcome to this quiz,", name)
print("This quiz is about countries")


while True:
    try:
      tries = input("How many attempts do you want at each question? ")
      tries = int(tries)
      print("Alright, you will now get {} tries for each question.".format(tries))
    except:
      print("That is not a number.")





         
# Ask the user a question