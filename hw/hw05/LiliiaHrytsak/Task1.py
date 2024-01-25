def convert_to_float(some_list):
    res_list = []
    for i in some_list:
        res_list.append(float(i))
    return res_list

print(convert_to_float([1,2,3]))