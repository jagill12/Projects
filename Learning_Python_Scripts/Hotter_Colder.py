def HotterColder():
    '''
    John Gill: Hotter Colder
    Dr. Lindsay
    CS5001
    This program asks the user to guess a number and gives feedback on whether
    each guess is hotter (closer) or colder (further) compared to the last.
    '''
    target = 42
    guess = int(input("Give me a positive number, Sonny: "))
    difference = abs(guess - target)

    while guess != target:
        new_guess = int(input("Wrong. Give me another number, Sonny: "))
        new_difference = abs(new_guess - target)

        if new_difference < difference:
            print("You're heating up, Sonny.")
        elif new_difference > difference:
            print("You're cooling down, Sonny.")
        else:
            print("Same distance, Sonny. Try harder!")

        guess = new_guess
        difference = new_difference

    print("YOU DID IT, SONNY!")

def main():
    HotterColder()

if __name__ == "__main__":
    main()
