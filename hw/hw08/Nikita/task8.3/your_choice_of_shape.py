from area import *

while True:
    shape = input('Choose one of the shape: Triangle, rectangle, circle: ')
    shape = shape.lower()

    match shape:
        case  'triangle':
            b = int(input('Enter your value: '))
            h = int(input('Enter your value: '))
            s = triangle(b,h) 
            break
        case 'rectangle':
            l = int(input('Enter your value: '))
            w = int(input('Enter your value: '))
            s = rectangle(l,w)
            break
        case 'circle':
            r = int(input('Enter your value: '))
            s = circle(r)
            break
        case _:
            print('Unknown shape. Try again, please! ')
            continue   
print(f'The{shape} square is: {s}')                             
