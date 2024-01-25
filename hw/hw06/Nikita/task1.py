l_o = []
l_e = []
l_n = []

for i in range(1,11):
    if i % 2 == 0:
        l_o.append(i)
    elif i % 3 == 0:
        l_e.append(i)
    else:
        l_n.append(i)

print('EVEN: ', l_o)
print('ODD: ', l_e)
print('Not divisible by 2 and 3: ', l_n)