def recur(x):
    '''fibonacci sequence. x equals the spot in the sequence, and will return the value at that spot'''
    if x <= 1:
        return x
    else:
        return recur(x - 1) + recur(x - 2)
        
def reverse(x):
    if(len(x) == 1):
        return x
    else:
        return x[len(x)-1] + reverse(x[0: len(x) - 1])

def recur_sum(x, y):
    if x == y:
        return x
    else: 
        return x + recur_sum(x + 1, y)


def main():
    '''print(recur(9))'''
    hello = "yellow"
    print(reverse(hello))
main()
