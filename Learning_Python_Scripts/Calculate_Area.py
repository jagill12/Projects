def calculate_area(width, height):
    try:
        if width <= 0:
            raise ValueError("Width must be positive.")
        if height <= 0:
            raise ValueError("Height must be positive.")
        return width * height
    except ValueError as e:
        if str(e) == "Width must be positive.":
            print("Invalid width input.")
        elif str(e) == "Height must be positive.":
            print("Invalid height input.")
        else:
            print("Invalid input.")
def main():
    print(calculate_area(0, 0))
    print(calculate_area(-15, -15))
    print(calculate_area(0, 15))
    print(calculate_area(15, 0))
    print(calculate_area(-15, 0))
    print(calculate_area(0, -15))
    print(calculate_area(15, 15))
main()
