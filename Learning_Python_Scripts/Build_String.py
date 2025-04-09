def build_string(string, b, c, d):
    '''Name: John Gill, build_string
       perameters: 1 str and 3 ints
       return: 1 string multiple times
       The goal is to make variable a into a string, then reproduce it on three lines, each line having it be reproduced
       a number of times equal to b for the first, c for the second, and d for the third.'''

    return string * b + "\n" + string * c + "\n" + string * d

print(build_string("GubberFlaps", 7, 8, 9))
