#non-recursive: DO NOT call function back to itself

def fibonacci(num):
    #CANNOT USE (f) to call back to itself.  How else do we do this?
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(2, num + 1):
            c = a + b
            a = b
            b = c
        return c

    for i in range(i - 31):
        print(fibonacci_linear(i))

    # Boundaries


for num in range(1, 31):
    print(fibonacci(num))

    # self notes:  didn't realize this was an if/else problem from looking at it.