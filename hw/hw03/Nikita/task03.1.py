def product(x):
    result = 0
    for i in x:
        result += int(i)

    return result

x = str(input('enter number: '))

print(f'product: {product(x)}')

print(f'Reverse number: {x[::-1]}')

sort = ''

while len(x) > 0:
    sort += min(x)
    index_min = x.find(min(x))
    x = x[:index_min] + x[index_min+1:]
print('Sorted number: ',sort)


















