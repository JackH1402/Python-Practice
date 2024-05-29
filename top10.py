# -----FUCTIONS-----
POPULATED_COUNTRIES_ANSWERS = ["india", "china", "usa", "indonesia", "pakistan", "nigeria", "brazil", "bangladesh", "russia", "mexico"]
def getLives():
    while True:
        lives = input ("How many chances do you want")
        try:
            lives = int(lives)
            if lives >= 0:
                return lives
            else:
                print("Please choose a positive number")
        except:
            print("That wasn't a number")

# Welcomes user and introduces the quiz
def intro():
    #Ask user their name
    name = input("What's your name")

    # Greets user and introduces the quiz
    print("Welcome to this quiz,", name)
    print("This quiz is about the ten most populated countries in the world. Can you name them?")

# ----- MAIN CODE -----

intro()
lives = getLives()
score = 0
while lives > 0:
    answer = input("Name one of the top 10 most populaqted countriesin the world:/n").lower()