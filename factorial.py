def factorials():
    x = input("Please enter a number:")
    num = 1
    for i in range(int(x), 1, -1):
        num *= i
        print(num)


factorials()