with open('zen.txt') as f:
    text_data = f.read()


def find_occur(input_str, *words):
    res_dict = dict()
    for word in words:
        res_dict[word] = input_str.count(word)
    return res_dict


def display_upper(input_str):
    res_str = input_str.upper()
    return res_str


def replace_occur(input_str,sub1, sub2):
    res_str = input_str.replace(sub1, sub2)
    return res_str


print(find_occur(text_data.lower(), 'better', 'never','is'))
print('\n\n')

print(display_upper(text_data))
print('\n\n')

print(replace_occur(text_data, 'i', '&'))