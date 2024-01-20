from area import *


input_value = input('Which area do you want to calculate: rectangle, triangle, or circle? ')
if input_value not in ['rectangle', 'triangle', 'circle']:
    print("Notvalid input")
else:
    if input_value == 'rectangle':
        area = rectangle_area(length=input("Write the length "), width=input("Write the width "))
    elif input_value == 'triangle':
        area = triangle_area(base=input("Write the base "), height=input("Write the height "))
    elif input_value == 'circle':
        area = circle_area(radius=input('Write radius '))
    print(f'Chosen area of {input_value} = {round(area,2)}')