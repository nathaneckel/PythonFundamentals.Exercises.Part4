def factorials():
    x = input("Please enter a number:")
    num = 1
    for i in range(int(x), 1, -1): #for # in range 1. userInput(STARTING #, STOPPING #, STEP #
        num *= i
        print(num)


factorials()