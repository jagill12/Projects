def my_function():
    print("Hello World!")
    
my_function()

def function_of_parameters(a):

    if a % 2 != 0:
        return True
    else:
        return False

print(function_of_parameters(13))

def eighteen_percent(b):

    return b * .18

print(eighteen_percent(6))



def get_pounds_weight(stone_weight):
    '''Function name: get_pounds_weight
        Parameters: 1 float
        Returns: float'''
    pounds = stone_weight * 14
    return pounds

def main():

    stone = 5.3
    tug_weight = get_pounds_weight(stone)
    print("Your dog weighs ", tug_weight, " pounds!")

main()
