play = "yes"

QUESTION_FORMAT = "{}\nA.{} B.{} C.{} D.{}"
GOOD_COMMENTS = ["Good job!", "Keep it up!", "Your on a roll!"]
BAD_COMMENTS = ["Unlucky", "Keep trying", "You need some help"]

QUESTIONS = ["What is the smallest country by land mass? ",
              "What country has the highest population? ",
                "What country has the lowest sea level? ",]

OPTIONS = [["San Marino", "Tonga", "Russia", "Vatican City"],
            ["Sri Lanka", "India", "China", "France"],
             ["Qatar", "Denmark", "New Zealand", "Maldives"]]
SHORT_OPTIONS = ["a", "b", "c", "d"]
ANSWERS = [3,1,3]

import random
score = 0

# Ask the user there name
name = input("What's your name? ")
# Greet the user and introduce the quiz
print("Welcome to this quiz,", name)
print("This quiz is about countries")

while True:
    try:
      tries = input("How many attempts do you want at each question? ")
      tries = int(tries)
      print("Alright, you will now get {} tries for each question.".format(tries))
      break
    except:
      print("That is not a number.")

while play == "yes":
  score = 0

  for i in range(len(QUESTIONS)):
    question_attempts = tries
    while question_attempts > 0:
      answer = input(QUESTION_FORMAT.format(QUESTIONS[i], OPTIONS[i][0],
                                              OPTIONS[i][1], OPTIONS[i][2], OPTIONS[i][3])).lower()
      
      if answer == OPTIONS[i][ANSWERS[i]] or answer == SHORT_OPTIONS[ANSWERS[i]]:
        print("Correct!")
        score += 1
        print("1 point has been added to your score, it is now {}.".format(score))
        break
      elif answer == "":
        print("Not sure?")
      elif answer in SHORT_OPTIONS or answer in OPTIONS[i]:
        print("Wrong!")
        print(random.choice(BAD_COMMENTS))
      else:
        print("That was not an option.")


      question_attempts -= 1

  print("Well done, you have completed the quiz. Your final score was {}.".format(score))

  play = input("Do you want to play again?")





         
# Ask the user a question