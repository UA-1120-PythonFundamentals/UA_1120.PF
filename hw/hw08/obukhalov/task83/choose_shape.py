#!/usr/bin/env python


from area_calculation import rectangle_square, triangle_square, circle_square


if __name__ == "__main__":

    print("Square calculator")

    while True:
        shape = input("Enter the shape's name. Rectangle, triangle or circle.: ")
        shape = shape.lower()

        match shape:
            case "rectangle":
                a = int(input("The lenght of the first side of rectangle is: "))
                b = int(input("The lenght of the second side of rectangle is: "))
                square = rectangle_square(a, b)
                break
            case "triangle":
                b = int(input("The base of the triangle is: "))
                h = int(input("The height of the triangle is: "))
                square = triangle_square(b, h)
                break
            case "circle":
                r = int(input("The radius of the circle is: "))
                square = circle_square(r)
                break
            case _:
                print("Innacceptable shape. Try again!")
                continue

    print(f"The {shape} square is {square}")
            
