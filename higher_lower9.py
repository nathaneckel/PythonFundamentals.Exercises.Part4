#   WHILE SUCCESS = FALSE keep playing the game!
#ELSE  print("My number is also " + str(random) + ". " + str(guess) + " \n YOU WIN!")

#this function asks user for a number 1-10
from random import randrange

def number_guessing_game():
    guess = int(input("Please enter a number (0 to 10)\n"))
    return(guess)

#Function: Generate and Return a Number
def random_number_generator():
    return randrange(10)


def high_or_low(random, guess):
    while True:
        random = guess()
        if(random == guess):
            print("My number is also " + str(random) + ". " + str(guess) + " \n YOU WIN!")
        elif(random < guess):
            if (random < guess):
                print(str(guess) + " was too high!\n Try again")
        elif (random > guess):
            print(str(guess) + " is too low!\n Try again!")
            break


#Call Main - This Runs the Program
main(number_guessing_game())