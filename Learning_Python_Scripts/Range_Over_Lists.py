'''def lists():
    for counter in range (1, 11):
        print("*" * counter)

def ListsReversed():
    count = 10
    while count >= 1:
        print("*" * count)
        count -= 1'''

def main():
    '''lists()
    ListsReversed()'''

    x = int(input("Enter row number = \n"))
    for i in range(x):
        for j in range(i + 1):
            print("#", end = '')
        print("")
main()
