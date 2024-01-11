n = 1324


def find_prod(inp_num):
    num_str = str(inp_num)
    res_num = 1
    for i in num_str:
        res_num *= int(i)
    return res_num


def reverse_oder(inp_num):
    num_str = str(inp_num)
    res_num = int(num_str[::-1])
    return res_num


def sort_num(inp_num):
    num_str = str(inp_num)
    res_num = int("".join(sorted(num_str)))
    return res_num


print(find_prod(n))
print(reverse_oder(n))
print(sort_num(n))