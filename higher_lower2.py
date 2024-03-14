#WHILE RANDOM !== GUESS, KEEP PLAYING (SEE BELOW)
#this function asks user for a number 1-10
from random import randrange

#Helper Functions
#Initiate the game
def number_guessing_game():
    guess = int(input("Please enter a number (0 to 10)\n"))
    return(guess)

#Function: Generate and Return a Number
def random_number_generator():
    return randrange(10)

#NEED A HINT / RETRY OPTION - COULD I REARRANGE THE ELIFS FOR THIS?
#Function: Compare Number for the Guess; Give Feedback


#   WHILE LOOP!!!
#   While guess !== keep playing the game!

def number_compare(random, guess):
    if(random == guess):
        print("My number is also " + str(random) + ". " + str(guess) + " \n YOU WIN!")
    elif(random < guess):
        if (random < guess):
            print(str(guess) + " was too high!\n Try again")
    elif (random > guess):
            print(str(guess) + " is too low!\n Try again!")

def number_guessing_game2():
     guess = int(input("Please enter a number (0 to 10)\n"))
     return(guess)

#Main Function - This Calls the Helpers In Order
def main():
    random = random_number_generator()
    guess = number_guessing_game()
    number_compare(random, guess)
    guess = number_guessing_game2()


#Call Main - This Runs the Program
main()