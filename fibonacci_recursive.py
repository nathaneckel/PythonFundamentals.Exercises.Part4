def fibonacci(f):
    if f == 1:
        return 0
    elif f == 2:
        return 1
    else:
        return fibonacci(f-1) + fibonacci(f-2)

    #Boundaries
for num in range(1, 31):
    print(fibonacci(num))