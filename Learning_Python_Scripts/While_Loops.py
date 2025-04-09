def loop():
    x = 0
    list = []
    print("Hello! I want you to give me five short words, less than five letters. You get ten tries. If you miraculously fail, you lose.")
    while x < 10 and len(list) < 5:
        if len(list) < 5:
            a = str(input("Give me a word: "))
            while len(a) > 4 and x < 9:
                print(9 - x, " guesses left")
                a = str(input("That was longer than 5 characters. Try again: "))
                x += 1
            list.append(a)
            print(list)
            print("You lose!")
        print(9 - x, " guesses left")
        print("Here are your words: ", list)
        x += 1
    if len(list) == 5:
        print("YOU WIN! Here are your words: ", list)
    if x == 10:
        print("You lose!")
def main():
    loop()
main()
