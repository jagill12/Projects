def PrintMax():
    '''John Gill. 
   We want to get the maximum number'''
    max = 0
    number = int(input("Give me a number"))
    while(number != -1):
        if number >= max:
            max = number
        number = int(input("Give me a number"))
    print("The max number is: ", max)    
        
PrintMax()
