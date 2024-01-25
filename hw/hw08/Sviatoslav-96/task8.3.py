import math

def rectangle_area(a, b):
    s = a * b
    return s

def triangle_area(a, h):
    S = 0.5 * h * a
    return S

def circle_area(r):
    S = math.pi * r**2
    return S

def main():
    choice = int(input("Enter the number for the figure (1 - rectangle, 2 - triangle, 3 - circle): "))

    if choice == 1:
        a = float(input("a = "))
        b = float(input("b = "))
        result = rectangle_area(a, b)
        print("Area of rectangle:", result)

    elif choice == 2:
        a = float(input("a = "))
        h = float(input("h = "))
        result = triangle_area(a, h)
        print("Area of triangle:", result)

    elif choice == 3:
        r = float(input("r = "))
        result = circle_area(r)
        print("Area of circle:", result)

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()