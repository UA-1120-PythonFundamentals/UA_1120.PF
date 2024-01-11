def integer_boolean(binary_number):
    bin_list = []
    for i in binary_number:
        if int(i) == 1:
            bin_list.append(True)
        else:
            bin_list.append(False)
    return bin_list

print(integer_boolean('100101'))