from random import randrange

#Prompting user to enter a number:
def yank_input():
    x = input("Pick a Number: \n")
    return int(x)

#Define random_num and randrange parameters
def rand_num():
    rand = randrange(1, 10)
    return rand

#Define high or low and boolean True loop

def high_or_low(random):
    while True: #this is the key boolean statement that makes the loop work - don't forget colon:
        playerOne = yank_input()
        print('Your number: ' +str(playerOne))
        if playerOne == 0:
            print("You guessed 0 -\n Try Again from 1 to 10!")
        if playerOne > random:
            print("You guessed too high!\n Try Again!")
        elif playerOne < random:
            print("You guessed too low\n Try Again!")
        elif playerOne == random:
            print("You guessed the number! \nYou Win!")
            break


#Call the high_or_low function to begin the game
high_or_low(rand_num())