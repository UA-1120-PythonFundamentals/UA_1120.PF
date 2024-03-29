from .calc import area_of_rectangle, area_of_triangle, area_of_circle

while True:
    figure = input("Enter the name of the geometric figure: ").lower()

    match figure:
        case "rectangle":
            length = float(input("Input the length of rectangle: "))
            width = float(input("Input the width of rectangle: "))
            print(f"Area of {figure} = {area_of_rectangle(length, width)}")
            break
        case "triangle":
            base = float(input("Input the base of triangle: "))
            height = float(input("Input the height of triangle: "))
            print(f"Area of {figure} = {area_of_triangle(base, height)}")
            break
        case "circle":
            radius = float(input("Input the radius of circle: "))
            print(f"Area of {figure} = {area_of_circle(radius)}")
            break
        case _:
            print(f"Error! Enter another figure!")
            continue
