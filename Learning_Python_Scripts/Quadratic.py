def Formula(a, b, c):
    '''Function: run three numbers through the quadratic formula
       Parameters: 3 floats
       Returns: 2 floats, the upper and lower limit'''
    x = (-b + ((b ** 2) - (4 * (a * c))) ** (1/2)) / (2 * a)
    y = (-b - (b ** 2 - (4 * (a * c))) ** (1/2)) / (2 * a)
    return x, y
