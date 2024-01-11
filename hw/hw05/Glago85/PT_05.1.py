#Changing the type of elements in a list from integer to a floating
my_list = [23, 19, 7, 85, 38, 20, 1, 24]
for x in range(0, len(my_list)):
    my_list[x] = float(my_list[x])
print(my_list)