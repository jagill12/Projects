import random

def WordGuesser(guess, word, revealed):
    result = ""
    for i in range(len(word)):
        if word[i] == guess:
            result += guess
        else:
            result += revealed[i]
    return result

def main():
    word = input("Give me a single word, no spaces: ").lower()
    instances = 6
    revealed = "*" * len(word)

    while instances > 0:
        print(f"Current word: {revealed}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        new_revealed = WordGuesser(guess, word, revealed)

        if new_revealed == revealed:
            instances -= 1
            print(f"Incorrect guess. You have {instances} attempts left.")
        else:
            print("Good guess!")
            revealed = new_revealed

        if revealed == word:
            print(f"You guessed it! The word was '{word}'.")
            break

    if revealed != word:
        print(f"You have failed. The word was '{word}'.")

main()
