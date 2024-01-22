from area import rect, trian, circle

figure = int(input('Choice rectangle - 1, triangle - 2 or circle - 3 '))
if figure == 1:
    print('Side lengths:')
    rect(input('first side: '), input('second side: '))
elif figure == 2:
    print('Altitude and side triangle: ')
    trian(input('altitude: '), input('side: '))
elif figure == 3:
    circle(input('Radius: '))
else:
    print('This figure is missing')
