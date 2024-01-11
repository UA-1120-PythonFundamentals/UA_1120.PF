import math

def calculate (user):
    if user == "restangle":
        restangle_A = input("Enter A:")
        restangle_B = input("Enter B:")
        print(f"restangle = {restangle_A * restangle_B}")
    elif user == "triangle":
        triangle_h = input("Enter h:")
        triangle_a = input("Enter a:")
        print(f"triangle = {0.5 * triangle_h * triangle_a}")
    elif user == "circle":
        circle_r = math.pow(int(input("Enter r:")),2)
        print(f"circle = {math.pi * circle_r}")
    else:
        print("Your answer invalid :0")

    