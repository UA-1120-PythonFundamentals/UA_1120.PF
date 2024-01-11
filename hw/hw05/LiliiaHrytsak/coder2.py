def binary(decimal):
    if decimal == 0:
        return '0'
    str_num = ''
    while decimal > 0:
        str_num = str(decimal%2) + str_num
        decimal = decimal // 2
    return str_num


print(binary(1000))