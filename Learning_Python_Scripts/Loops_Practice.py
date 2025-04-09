def computeAverage():

    num_inputs = 0
    total = 0
    grade = int(input("Enter your grade or -1 to quit"))
    while(grade != -1):
        total += grade #total = total + grad
        num_inputs += 1 #num_inputs = num_inputs + 1
        grade = int(input("Enter your grade or -1 to quit"))
    if (num_inputs != 0):
        average = total / num_inputs
    else:
        average = total
    print("The average grade was: " + str(average))

computeAverage()
