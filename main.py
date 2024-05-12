QUESTION_FORMAT = "{}\nA.{} B.{} C.{} D.{}"
score = 0
# Ask the user there name
name = input("What's your name?")
# Greet the user and introduce the quiz
if name == "Jack":
  print("What a silly name!")
else:
  print("I don't know that name, who are you?")
print("Welcome to this quiz,", name)
print("This quiz is about countries")
# Ask the user a question
answer = input("What is the smallest country by land mass?").lower()
# Tell the user the answer
if answer == "Vatican City" .lower():
  print("Correct! Good job +1")
  score+= 1
else:
  print("Wrong! Unlucky -1")
  print("The answer is Vatican City.")
  score-= 1
# Ask the user another question
 ("What country has the highest population?").lower()
# Tell the user the answer
if answer == "India" .lower():
  print("Correct! Keep it up +1")
  score+= 2
else:
  print("Wrong! You got to try harder -1")
  print("the answer is India with 1.4 billion")
  score-= 2
# Ask the user another question
question = ("What country has the lowest sea level?").lower()
a = "Qatar"
b = "Denmark"
c = "Maldives"
d = "New Zealand"
answer = input(QUESTION_FORMAT.format(question, a, b, c, d)).lower()
# Tell the user the answer
if answer == c or answer == "c":
  print("Correct! You are on a roll +1")
  score+=3
else:
  print("Wrong! You may want to learn Geography -1")
  print("The answer is Maldives at 1.8m or 6ft")
  score-=3
print("Well done. That's the end. You got ", score, "points")
print("Well done {}. You finished this quiz. Your final score was {}".format(name, score))