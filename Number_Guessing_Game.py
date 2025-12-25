import random

def number_guessing_game():
    print("Welcome to Number Guessing Game")
    print("I chose a random number between 1 and 100.")

    choosen_number = random.randint(1, 100)
    chance_of_prediction = 5
    
    while chance_of_prediction > 0:
        try:
            #take a chance from user
            user_chance=int(input("what is your chance?"))
        except ValueError:
            print("Please try again")
            continue
        if user_chance ==choosen_number:
            print("Congratulations! You won.")
            break
        elif user_chance > choosen_number:
            print("you should choose a lower number")
        else:
            print("you should choose a higher number")
        
        chance_of_prediction-=1
    if chance_of_prediction==0:
        print(f"I am sorry. Game over.The choosen number is:{choosen_number}")

#you can start the game
number_guessing_game





