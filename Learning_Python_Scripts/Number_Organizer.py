'''This program's aim is to organize 3 different numbers 
    that the user inputs in order from largest to smallest.'''

def main():
    print("Give me 3 numbers. Once you do, I'll organize them from largest to smallest, then tell you the average of all three.")
    a = int(input("First number: "))
    b = int(input("Second number: "))
    c = int(input("Third number: "))

    '''Now we will create a series of if statements that seek to 
    arrange these 3 numbers in descending order. Then we will calculate the average.'''

    if a > b:
        if a > c:
            if b > c:
                print(a, b, c)
            elif c > b:
                print(a, c, b)
        elif c > a:
            print(c, a, b)
    elif b > a:
        if a > c:
            print(b, a, c)
        elif b > c:
            print(b, c, a)
        else:
            print(c, b, a)
    average = (a + b + c)/3
    print("The average is ", average)
    print("Done.")
main()
