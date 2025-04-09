'''
This file will be used in Project 3.
John Gill
Due 2/4/2023
This project makes the computer print out a random card from a standard deck.
'''

import random
import sys

def GetSuit():
    '''Returns a random suit.'''
    suit = random.randint(1, 4)
    if suit == 1:
        return "Hearts"
    elif suit == 2:
        return "Spades"
    elif suit == 3:
        return "Diamonds"
    else:
        return "Clubs"

def GetValue():
    '''Returns a random card value.'''
    number = random.randint(1, 13)
    if number == 1:
        return "Ace"
    elif number == 11:
        return "Jack"
    elif number == 12:
        return "Queen"
    elif number == 13:
        return "King"
    else:
        return str(number)

def PrintCard(value, suit):
    '''Prints the card.'''
    print(f"{value} of {suit}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 cardFunctions.py [red or black]")
        return

    color = sys.argv[1].lower()
    value = GetValue()
    suit = GetSuit()

    PrintCard(value, suit)

    # Check for match
    if color == "red":
        if suit in ("Hearts", "Diamonds"):
            print("Match! The color matches the card.")
        else:
            print("No match. The card is black.")
    elif color == "black":
        if suit in ("Spades", "Clubs"):
            print("Match! The color matches the card.")
        else:
            print("No match. The card is red.")
    else:
        print("Invalid entry. Please enter 'red' or 'black'.")

if __name__ == "__main__":
    main()
