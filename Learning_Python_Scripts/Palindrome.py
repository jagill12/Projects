def Palindrome(word):
    '''The goal of this program is to determine whether a word 
    we give it is a palindrome.'''
    x = len(word)-1
    y = 0

    while x > y:

        if word[y] == word[x]:
            x -= 1
            y += 1
        else:
            x = 0
    if y >= .5 * (len(word)-1):
        print("That sucker's a palindrome.")
    else:
        print("Not a palindrome.")
        
def Count(object, my_char):
    x = len(object)-1
    y = 0
    count = 0
    while y <= x:
        if y == my_char:
            count += 1
        y += 1
    print("Your character appeared " + count + "times in your chosen input.")

    times = 0
    count = 0
    while(count < len(object)-1):
        if(object[count] == my_char):
            times += 1
        count += 1
    print("Your character appeared" + times + " times.")
        


def main():

    '''word = "racecar"
    Palindrome(word)'''

if __name__ == "__main__":
    main()
