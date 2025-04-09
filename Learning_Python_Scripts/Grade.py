def grade(a):

    '''Name: John Gill, grade
       Perameter: 1 float
       Returns: 1 string
       We will be determining what grade value is assigned to what score we give the computer.'''

    if a >= 92:
        return ("A+! :>")
    elif a >= 90 and a <= 91:
        return ("A-. :)")
    elif a >= 87 and a <= 89:
        return ("B+ :')")
    elif a >= 82 and a <= 86:
        return ("B :')")
    elif a >= 80 and a <= 81:
        return ("B- :')")
    elif a >= 65 and a <= 79:
        return ("C(ish) :(")
    elif a <= 64:
        return ("Utter failure. :'<")

print(grade(30))
