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
answer = input("What is the smallest country by land mass?")
# Tell the user the answer
if answer == "Vatican City":
  print("Correct! Good job +1")
  score+= 1
else:
  print("Wrong! Unlucky -1")
print("The answer is Vaitcan City.")
score -= 1
# Ask the user another question
answer = input("What country has the highest population?")
# Tell the user the answer
print("the answer is India with 1.4 billion")
if answer == "India":
  print("Correct! Keep it up +1")
  score+= 2
else:
  print("Wrong! You got to try harder -1")
  score-= 2
# Ask the user another question
answer = input("What country has the lowest sea level?")
# Tell the user the answer
if answer == "The Maldives":
  print("Correct! You are on a roll +1")
  score+=3
else:
  print("Wrong! You may want to learn Geography -1")
  print("The answer is Maldives at 1.8m or 6ft")
  score-=3