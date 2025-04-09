def area_triangle(a, b, c):
    
    '''Name: Area_triangle, John Gill
       Parameters: 3 ints
       Returns: 1 float
       We are calculating the area of a triangle'''

    s = (a + b + c) // 2
    
    A = (s * (s-a) * (s-b) * (s-c)) ** (1/2)
    
    return A

print(area_triangle(3, 5, 6))
