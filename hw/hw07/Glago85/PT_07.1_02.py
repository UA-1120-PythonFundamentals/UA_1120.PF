#Write a program that calculates the area of a rectangle, triangle and circle
#(write three functions to calculate the area, and call them in the main program depending on the user's choice).

def area_rectangle(l, w):
    """Calculation of the area of a rectangle, where
    l - is the length of the rectangle,
    w - is the width of the rectangle."""
    return round(l * w, 2)

def area_triangle(b, h):
    """Calculation of the area of a triangle, where
    b - is the base of the triangle,
    h - is the height of the triangle."""
    return round((b * h) / 2, 2)

def area_circle(r):
    """Calculation of the area of a circle, where
    r - is the radius of the circle."""
    PI = 3.141592
    return round(PI * r ** 2, 2)

#Main program
figure = input("Choose a shape: rectangle, triangle or circle: ")
figure = figure.lower()

if figure == "rectangle":
    l = float(input("Enter the length of the rectangle: "))
    w = float(input("Enter the width of the rectangle: "))
    area = area_rectangle(l, w)
elif figure == "triangle":
    b = float(input("Enter the base of the triangle: "))
    h = float(input("Enter the height of the triangle: "))
    area = area_triangle(b, h)
elif figure == "circle":
    r = float(input("Enter the radius of the circle: "))
    area = area_circle(r)
else:
    print("Invalid choice")
    area = None
    
if area is not None:
    print(f"The area of the {figure} is {area}.")