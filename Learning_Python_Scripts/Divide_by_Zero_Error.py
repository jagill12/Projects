def main():
    x = 0
    while x == 0:
        try:
            x = int(input("Enter a number to divide 10 by: "))
            quotient = 10 / x
            print("The quotient is: ", quotient)
        except ZeroDivisionError:
            print("Error: can't divide by zero.")
main()
