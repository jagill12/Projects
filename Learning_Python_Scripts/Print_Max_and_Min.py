def PrintMaxAndMin():

    FirstNumber = int(input("Give me a number, or give me -1 to stop: "))
    while (FirstNumber != -1):
        max_num = FirstNumber
        min_num = FirstNumber
        SecondNumber = int(input("Now give me a second number: "))
        if SecondNumber > max_num:
            max_num = SecondNumber
        elif SecondNumber < min_num:
            min_num = SecondNumber
        print("The max number is ", max_num, "and the min number is ", min_num)
        FirstNumber = int(input("Give me a number, or give me -1 to stop: "))
PrintMaxAndMin()
