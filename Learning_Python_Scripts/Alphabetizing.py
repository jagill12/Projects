'''The goal of this program is to give it four random words, and
then have the program alphabetize them.'''
def main():
    print("Tell me four different words.") 
    '''For simplicity, we're making the inputs be simple letters.'''
    a = str(input("Word number one: "))
    b = str(input("Word number two: "))
    c = str(input("Word number three: "))
    d = str(input("Word number four: "))

    '''Let's find out the alphabetical order of these puppies. 
    These sweet little baby hush puppies. Please don't dock
    points for me being a dingus.'''

    if a < b:
        if a < c:
            if a < d:
                if b < c:
                    if b < d:
                        if c < d:
                            print(a, b, c, d)
                        else:
                            print(a, b, d, c)
                    elif b > d:
                        print(a, d, b, c)
                elif c < d:
                    if b < d:
                        print(a, c, b, d)
                    else:
                        print(a, c, d, b)
                else:
                    print(a, d, c, b)
            elif c < b:
                print(d, a, c, b)
            else:
                print(d, a, b, c)
        elif a < d:
            if d < b:
                print(c, a, d, b)
            else:
                print (c, a, b, d)
        elif c < d:
            print(c, d, a, b)
        else:
            print(d, c, b, a)
    elif a < c:
        if a < d:
            if c < d:
                print(b, a, c, d)
            else:
                print(b, a, d, c)
        elif b < d:
            print(b, d, a, c)
        else:
            print(d, b, a, c )
    elif b < c:
        if d < c:
            if b < d:
                print(b, d, c, a)
            else:
                print(d, b, c, a)
        elif a < d:
            print(b, c, a, d)
        else:
            print( b, c, d, a)
    elif c < d:
        if b < d:
            if d < a:
                print(c, b, d, a)
            else:
                print(c, b, a, d)
        else:
            print(c, d, b, a)
    else:
        print(d, c, b, a)
print("Done.")

main()
