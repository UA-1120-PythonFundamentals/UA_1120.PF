
def calc_characters(s):
    d = {}
    for i in s:
        d[i] = d.get(i, 0) + 1
    return d

print(calc_characters(input('Enter string: ')))
