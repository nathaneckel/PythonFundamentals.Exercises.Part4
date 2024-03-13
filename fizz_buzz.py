#Printing each number 1-100 to a new line
def fizz_buzz():
    for i in range(101): #This program will print each i (number) from 1 to 100 in a new line.

        if i % 3 == 0 and i % 5 == 0:
            print(str(i) + " FizzBuzz")
            continue

        elif i % 3 == 0:
            print(str(i) + " Fizz")
            continue

        elif i % 5 == 0:
            print(str(i) +" Buzz")

        else:
            print(str(i))

#Calling the main program
fizz_buzz()